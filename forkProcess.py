import subprocess
import resource
import sys
import os

def fork_process(cmd):
    pid = None
    success = False
    try:
        pid= os.fork()
    except OSError, e:
        print >>sys.stderr, "Error: os.fork() failed: %s" % e
        return None
    if pid == 0:  # Child
        # Do not allow child to inherit open file descriptors from parent.
        max_fd = resource.getrlimit(resource.RLIMIT_NOFILE)[0]
        for i in range(3, max_fd):
            try:
                os.close(i)
            except OSError:
                pass
        # Now start process
        # Tasks in child process
        subprocess.call(cmd)
        sys.exit()
    else:   # Parent
        return pid

