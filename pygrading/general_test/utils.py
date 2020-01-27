import time
import subprocess
from typing import Tuple


def bash(cmd: str) -> Tuple:
    """Run a shell command

    Run a shell command with bash.

    Args:
        cmd: A command string.

    Returns:
        status: 0 for success, 1 for fail
        output: running log from bash
        exec_time: command execute time
    """
    begin = time.time()
    status, output = subprocess.getstatusoutput(cmd)
    end = time.time()
    exec_time = end - begin

    return status, output, exec_time
