import platform
import shutil
import subprocess
import sys


def command_version(command):
    path = shutil.which(command)
    if path is None:
        return None, None
    try:
        result = subprocess.run(
            [command, "--version"],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
        first_line = (result.stdout or result.stderr).splitlines()
        return path, first_line[0] if first_line else "version unavailable"
    except Exception as exc:
        return path, f"version check failed: {exc}"


def main():
    print("System")
    print(f"  platform: {platform.platform()}")
    print(f"  python: {sys.version.split()[0]}")
    print(f"  executable: {sys.executable}")

    print("\nTools")
    for command in ["git", "nvidia-smi"]:
        path, version = command_version(command)
        if path is None:
            print(f"  {command}: not found")
        else:
            print(f"  {command}: {path}")
            print(f"    {version}")

    try:
        import torch

        print("\nPyTorch")
        print(f"  torch: {torch.__version__}")
        print(f"  cuda available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"  cuda device count: {torch.cuda.device_count()}")
            print(f"  first device: {torch.cuda.get_device_name(0)}")
    except Exception as exc:
        print("\nPyTorch")
        print(f"  not available or failed to import: {exc}")


if __name__ == "__main__":
    main()

