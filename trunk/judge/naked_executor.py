#!/usr/bin/python

"""The NakedExecutor is an exector which doesn't use an advanced jailing
techniques.  Instead it uses as much as protection against rogue code
as it can muster on a default Unix system.

It should be sufficient for running trusted but possibly stupid code,  but it
isn't sufficient for running a public contest over the internet."""

import judge_logger
import resource_limit
import logging
import os
import random
import resource
import shutil
import sys
import subprocess
import time

logger = logging.getLogger('judge')

class NakedExecutor:
    """The NakedExecutor runs code using standard Unix jailing techniques."""

    def __init__(self, allow_insecurity = False):
        """@param allow_insecurity Should gaping vulnerabilities be allowed?"""
        self._allow_insecurity = allow_insecurity

    def capture_stdout(self, cmd):
        """ @return the output of cmd as a string """
        output, res = self.capture_stdout_and_resource_usage(cmd)
        return output

    def capture_stdout_and_resource_usage(self, cmd):
        """ @return tuple containing the output as a string and the
        resource usage """
        run_dir = self._get_run_dir()
        os.mkdir(run_dir)
        output_file_name = self._get_output_filename()
        resource_lim = resource_limit.ResourceLimit(cpu_lim = 1,
                                                    mem_lim = 32 << 20)
        forked_pid = os.fork()
        logger.debug("got pid %d" % forked_pid)

        if forked_pid == 0:  # child
            logger.debug('in child')
            resource_lim.enforce_limits()
            self._run_jailed_child_and_exit(cmd, run_dir, output_file_name)
            assert False, "jailed child should have exited"

        full_output_path = run_dir + '/' + output_file_name
        logger.debug('parent before wait')
        ret = os.waitpid(forked_pid, 0)
        logger.debug('parent after wait, reading from %s' % full_output_path)
        res_usage = resource.getrusage(resource.RUSAGE_CHILDREN)
        try:
            return open(full_output_path, 'r').read(), res_usage
        except IOError, e:
            return '', res_usage
    
    def _get_run_dir(self):
        """ @return The directory that this judger should use for its
        chroot."""
        # This should be a function of judge id, just use a random name for now
        return '/tmp/' + str(random.randint(0, 10000000))

    def _get_output_filename(self):
        return 'actual_out'

    def _executable_in_path(self, filename):
        """ @return true iff filename is readable and executable in PATH """
        path = os.getenv('PATH')
        for prefix in path.split(':'):
            full_path = os.path.expanduser(prefix + '/' + filename)
            if os.access(full_path, os.R_OK | os.X_OK):
                return True
        return False

    def _chroot_or_chdir(self, dir):
        """ Change root or change directory to dir.  Chroot is attempted
        first, since it is much more secure, but chroot requires
        privileges that usually only root has. """
        try:
            os.chroot(dir)
        except OSError, noperms:
            if self._allow_insecurity:
                os.chdir(dir)
                return
            raise SecurityException("Judger cannot chroot and refuses to "
                                    "chdir because insecurity is not allowed")

    def _wait_for_child_and_judge(self, child_pid, expected, full_output_name):
        pass  # TODO(rrenaud): delete?
        #time.sleep(.1)
        # Maybe we should check ret[1], which stores childs exit status.


    def _split_arglist(self, arglist):
        """Split arglist into a list of whitespace delimited strings, except
        that double quoted substrings are placed in a single element in the
        returned list, with the quotes removed.

        GOTCHAS: This doesn't group quoted strings which are not
        'well-delimited'.  By well-delimited, we mean a quoted string whose
        opening quote is bordered to the left by whitespace, and whose closing
        quote is bordered to the right by whitespace.
        f"o" and "fo"o are both not well-delimited.

        Here are a few correct usage input/output to the function.
        
        'hi' -> ['hi']
        'echo 1' -> ['echo', '1']
        'echo "quoted string" more'  -> ['echo', 'quoted string', 'more']
        """
        split_at_space = [x for x in arglist.split(' ') if len(x) > 0]
        ret = []
        have_unclosed_quote = False
        for item in split_at_space:
            # Special case a quoted string containing no delimiters.
            if len(item) == 1 and item[0] == '"' and item[-1] == '"':
                ret.append(item[1:-1])
                continue
                
            if not have_unclosed_quote and item[0] == '"':
                item = item[1:]
                # Make an new entry in the list to collect quoted string.
                ret.append('')  
                have_unclosed_quote = True
                
            if have_unclosed_quote:
                if len(item) > 0 and item[-1] == '"':
                    item = item[:-1]
                    have_unclosed_quote = False
                if len(ret[-1]) > 0: ret[-1] += ' '
                ret[-1] += item
            else:
                ret.append(item)
                
        return ret

    def _run_jailed_child_and_exit(self, cmd, run_dir, output_file_name):
        try:
            self._chroot_or_chdir(run_dir)
            # TODO(rrenaud): support running as a different user,
            # change to "jailed" user.
            # Call _exit rather than exit since exit raises a SystemExit,
            # and we want to be more discrete.  If the ordinary exit is
            # called, then pyunit will catch systemExit, which causes
            # the unittest to fail.
            args = self._split_arglist(cmd)
            logger.info("running cmd " +  cmd)
            access_error_msg = "Could find " + args[0] + " in PATH (" + \
                               os.getenv('PATH') + ")"
            assert self._executable_in_path(args[0]), access_error_msg
            judged_proc = subprocess.Popen(args, stdout = subprocess.PIPE,
                                           close_fds = True)
            # I thought about using a pipeline for juding and using
            # return codes for determining correctness, like
            # ./submitted_binary < file | judger,
            # but untrusted submitted binary can simply replace the judger
            # program with 'exit 0' and then their malicious program would
            # be correct.
            # To avoid this, the output of the submitted binary is
            # copied to a file, and then the judger runs from the
            # parent (protected for the submitted code , hopefully, by
            # at least a chroot and different user).
            output_file = open(output_file_name, 'w')
            shutil.copyfileobj(judged_proc.stdout, output_file)
            output_file.close()
            logger.debug('copied to %s/%s' % (run_dir, output_file_name))
            assert os.access(output_file_name, os.R_OK)

            if logger.isEnabledFor(logging.DEBUG):
                print 'debugging'
                logger.debug('Child: file contents %s' % (
                    open(output_file_name, 'r').read()))
            os._exit(0)
        except SecurityException:
            os._exit(1)


            
class SecurityException(Exception):
    """ A SecurityException is raised when the judge refuses to continue
    due to some sort of security violation"""
    pass
