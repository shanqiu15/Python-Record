import os
import subprocess, signal
p = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
out, err = p.communicate()
for line in out.splitlines():
    if  "process-name" in line:
        pid = int(line.split()[1])
        os.kill(pid, signal.SIGKILL)

