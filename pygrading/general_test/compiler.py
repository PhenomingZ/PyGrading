import subprocess
from typing import Tuple


def compile_c(source: str, target: str, compiler_type: str = "gcc", option: str = "-O2 -Wall -std=c90") -> Tuple:
    """Compile c source file

    Compile c source file using gcc.

    Args:
        source: c source file directory.
        target: target file path.
        compiler_type: (optional)compiler type, default gcc.
        option: (optional)addition options, default "-O2 -Wall -std=c90".

    Returns:
        status: compile status, 0 is success, 1 is fail.
        log: compile log
    """
    cmd = " ".join([str(compiler_type), str(option), str(source), "-o", str(target)])

    try:
        pass
    except Exception:
        pass


    return cmd
