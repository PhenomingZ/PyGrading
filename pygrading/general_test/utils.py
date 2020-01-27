import os
import time
import shutil
import subprocess
from typing import Tuple, List


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
    exec_time = int((end - begin) * 1000)

    return status, output, exec_time


def copyfile(src: str, dst: str):
    """Copy File"""
    shutil.copyfile(src, dst)


def copytree(src: str, dst: str):
    """Copy Tree"""
    shutil.copytree(src, dst)


def move(src: str, dst: str):
    """Move File"""
    shutil.move(src, dst)


def rmtree(src: str):
    """Remove Tree"""
    shutil.rmtree(src)


def rmfile(src: str):
    """Remove File"""
    os.remove(src)


def rename(old: str, new: str):
    """Rename File"""
    os.rename(old, new)


def readfile(src: str) -> str:
    """
    Read file and return string with \n.
    Auto remove blank line at the end of the file
    """
    cmd = ["cat", src]
    ret = bash(" ".join(cmd))
    return ret[1]


def writefile(src: str, lines: str):
    """
    Write string to file
    """
    with open(src, 'w', encoding='utf-8') as f:
        f.write(lines)


def readfile_list(src: str) -> List:
    """
    Read file and return list.
    Auto remove blank line at the end of the file
    """
    with open(src, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i].rstrip('\n')

        while "" == lines[-1]:
            lines.pop()

        return lines


def writefile_list(src: str, lines: List):
    """
    Write string list to file
    """
    with open(src, 'w', encoding='utf-8') as f:
        f.writelines(lines)


def compare_str(str1: str, str2: str) -> bool:
    return str1.rstrip() == str2.rstrip()
