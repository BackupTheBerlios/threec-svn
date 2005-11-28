#!/usr/bin/python
"""The ResourceLimit class represents the amount of resources that a process
can use.  It contains methods for setting the resources used by the process,
as well as checking which resource was exceeded."""

import resource

class ResourceLimit:
    """The ResourceLimit class is lazy, setting limits has no effect on
    the process until enforce_limits is called."""

    def __init__(self, mem_lim = 32 << 20, num_proc = 10, cpu_lim = 10):
        """Create a Resourcelimit with the given constraints on memory,
        number of processes, and CPU limit.  Note that this will NOT
        set the limits, you must call enforce_limits() to actually set the
        limit."""
        self._mem_lim = mem_lim
        self._num_proc = num_proc
        self._cpu_lim = cpu_lim

    def enforce_limits(self):
        """Ensure that this process cannot exceed our current
        ResourceLimit."""
        self._set_lim(resource.RLIMIT_CPU, self._cpu_lim)
        self._set_lim(resource.RLIMIT_AS, self._mem_lim)
        #self._set_lim(resource.RLIMIT_NPROC, self._num_proc)

    def exceeds_limits(self, rusage):
        """Return true iff rusage which is of type resource.struct_rusage
        exceeds the current memory limit"""
        pass
        
    def _set_lim(self, lim_type, lim_val):
        resource.setrlimit(lim_type, (lim_val, lim_val))

