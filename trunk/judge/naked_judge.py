#!/usr/bin/python

"""The NakedJudge is a judger which doesn't use an advanced jailing
techniques.  Instead it uses as much as protection against rogue code
as it can muster on a default Unix system.

It should be sufficient for a local contest where the contestants are
trusted, but it probably isn't sufficient for running a public contest
over the internet."""

import os
import random
import resource
import sys

class NakedJudge:
    """The NakedJudge runs code using standard Unix jailing techniques."""

    def __init__(self, allow_insecurity = False):
        """@param allow_insecurity Should gaping vulnerabilities be allowed?"""
        self._allow_insecurity = allow_insecurity
    
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
            raise SecurityException("Judger cannot chroot and refuses to"
                                    "chdir because insecurity is not allowed")

    def judge_exact(self, cmd, expected):
        """ @return JudgeResult containing the result of running cmd against
        expected output.  Run is successful only if the actual output is
        an exact match."""
        run_dir = self.get_run_dir()
        os.mkdir(run_dir)
        output_file_name = self.get_output_filename()

        self.child_pid = os.fork()

        if self.child_pid:  # parent
            ret = os.waitpid(self.child_pid, 1)
            # Maybe we should check ret[1], which stores childs exit status.
            try:
                child_usage = resource.getrusage(resource.RUSAGE_CHILDREN)
                path_to_output = run_dir + '/' + output_file_name
                output_lines = open(path_to_output, 'r').readlines()
                file_contents = ''.join(output_lines)
                if file_contents == expected:
                    return True
                else:
                    print "No match actual [[", file_contents, "]] and " \
                          "expected [[", expected, "]]"
                    return False
                
            except IOError, e:
                print 'in child of parent of judge_exact', e
                return False  # Couldn't read file?
                
        else:  # child
            # set resource limits with resource module
            try:
                self.chroot_or_chdir(run_dir)
                # Call _exit rather than exit since exit raises a SystemExit,
                # and we want to be more discrete.  If the ordinary exit is
                # called, then pyunit will catch systemExit, which causes this
                # test to fail.
                # Maybe we should use subprocess rather than system, so
                # no shell calls are performed.
                os._exit(os.system('(' + cmd + ') >' + output_file_name))
                #os.sl
            except SecurityException:
                os._exit(1)

            
class SecurityException(Exception):
    """ A SecurityException is raised when the judge refuses to continue
    due to some sort of security violation"""
    pass
