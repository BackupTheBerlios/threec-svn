#!/usr/bin/python

"""The NakedJudge is a judger which doesn't use an advanced jailing
techniques.  Instead it uses as much as protection against rogue code
as it can muster on a default Unix system.

It should be sufficient for a local contest where the contestants are
trusted, but it probably isn't sufficient for running a public contest
over the internet."""

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
logger.setLevel(logging.DEBUG)

class NakedJudge:
    """The NakedJudge runs code using standard Unix jailing techniques."""

    def __init__(self, allow_insecurity = False):
        """@param allow_insecurity Should gaping vulnerabilities be allowed?"""
        self._allow_insecurity = allow_insecurity

    def judge_exact(self, cmd, expected):
        """ @return JudgeResult containing the result of running cmd against
        expected output.  Run is successful only if the actual output is
        an exact match."""
        run_dir = self.get_run_dir()
        os.mkdir(run_dir)
        output_file_name = self.get_output_filename()
        resource_lim = resource_limit.ResourceLimit(cpu_lim = 1,
                                                    mem_lim = 32 << 20)
        forked_pid = os.fork()
        logger.debug("got pid %d" % forked_pid)

        if forked_pid:  # parent
            full_output_path = run_dir + '/' + output_file_name
            return self._wait_for_child_and_judge(forked_pid,
                                                  expected, full_output_path)

        else:  # child
            logger.debug('in child')
            resource_lim.enforce_limits()
            self._run_jailed_child_and_exit(cmd, run_dir, output_file_name)
            assert False, "jailed child should have exited"
    
    def get_run_dir(self):
        """ @return The directory that this judger should use for its
        chroot."""
        # This should be a function of judge id, just use a random name for now
        return '/tmp/' + str(random.randint(0, 10000000))

    def get_output_filename(self):
        return 'actual_out'

    def chroot_or_chdir(self, dir):
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
        logger.debug('parent before wait')
        ret = os.waitpid(child_pid, 0)
        logger.debug('parent after wait')
        #time.sleep(.1)
        # Maybe we should check ret[1], which stores childs exit status.
        try:
            child_usage = resource.getrusage(resource.RUSAGE_CHILDREN)
            logger.debug('Parent: reading ' +  full_output_name)
            output_lines = open(full_output_name, 'r').readlines()
            file_contents = ''.join(output_lines)
            if file_contents == expected:
                return True
            else:
                logger.debug("No match actual [[ %s]] and expected [[ %s ]]"
                              % (file_contents, expected))
                return False

        except IOError, e:
            logger.debug('in parent of judge_exact' + str(e))
            return False  # Couldn't read file?

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
            self.chroot_or_chdir(run_dir)
            # change to "judged" user
            # Call _exit rather than exit since exit raises a SystemExit,
            # and we want to be more discrete.  If the ordinary exit is
            # called, then pyunit will catch systemExit, which causes this
            # test to fail.
            # Maybe we should use subprocess rather than system, so
            # no shell calls are performed.
            args = self._split_arglist(cmd)
            logger.info("running cmd " +  cmd)
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
            logger.debug('Child: file contents %s' % (
                open(output_file_name, 'r').read()))
            os._exit(0)
        except SecurityException:
            os._exit(1)


            
class SecurityException(Exception):
    """ A SecurityException is raised when the judge refuses to continue
    due to some sort of security violation"""
    pass
