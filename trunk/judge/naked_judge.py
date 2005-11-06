#!/usr/bin/python

import os
import random
import resource
import sys

class NakedJudge:
    """ The NakedJudge runs code using standard unix jailing techiques.
    It should be sufficient for a local contest where the contestants are
    trusted, but it probably isn't sufficient for running a public contest
    over the internet. """

    def __init__(self, allow_insecurity = False):
        self._allow_insecurity = allow_insecurity

    
    def get_run_dir(self):
        """ @return the directory that this judeger should use for its
        chroot"""
        # This should be a function of judge id, just use a random name for now
        return os.tmpnam()

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
        raise SecurityError

    def judge_exact(self, cmd, expected):
        """ @return JudgeResult containing the result of running cmd against
        expected output.  Run is successful only if there actual output is
        an exact match."""
        run_dir = self.get_run_dir()
        os.mkdir(run_dir)
        output_file_name = self.get_output_filename()

        self.child_pid = os.fork()

        if self.child_pid:  # parent
            ret = os.waitpid(self.child_pid, 1)
            print ret
            
        else:  # child
            # set resource limits with resource
            self.chroot_or_chdir(run_dir)

            os.system(cmd + '>' + output_file_name)
            sys.exit(0)
            
            


    
    
