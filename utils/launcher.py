import ctypes
import os
import subprocess


ERROR_ELEVATION_REQUIRED = 740


def launch_exe(path: str):
    workdir = os.path.dirname(path)
    try:
        subprocess.Popen([path], cwd=workdir)
        return
    except OSError as exc:
        if getattr(exc, "winerror", None) != ERROR_ELEVATION_REQUIRED:
            raise

    result = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", path, None, workdir, 1
    )
    if result <= 32:
        raise OSError(f"ShellExecuteW failed with code {result}")
