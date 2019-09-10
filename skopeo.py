import os
import stat
import sys
import platform

PLATFORM = platform.system().lower()
BASE_DIR = os.path.dirname(__file__)
SKOPEO_PATH = f'lib/skopeo_{PLATFORM}'
SKOPEO_EXECUTABLE_SYSTEM = os.path.join(sys.prefix, SKOPEO_PATH)
SKOPEO_EXECUTABLE_LOCAL = os.path.join(BASE_DIR, SKOPEO_PATH)
SKOPEO_EXECUTABLE = (
    SKOPEO_EXECUTABLE_SYSTEM
    if os.path.exists(SKOPEO_EXECUTABLE_SYSTEM)
    else SKOPEO_EXECUTABLE_LOCAL
)

def main():
    print(SKOPEO_EXECUTABLE)
    args = [] if len(sys.argv) < 2 else sys.argv[1:]
    os.execv(SKOPEO_EXECUTABLE, ['skopeo', '--insecure-policy'] + args)
