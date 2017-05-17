"""
Unregister the given script in /usr/local/bin/registered
"""

import argparse
import os
import pathlib
import subprocess

from register import settings


def unregister(name):
    names = subprocess.check_output(['ls', settings.TARGET]).decode('utf-8').strip().split()
    if name not in names:
        print("[-] Script does not exist, or is not registered in {}: {}".format(settings.TARGET, name))
        return

    # don't check that path exists -- it might be a broken link
    path = settings.TARGET / name

    os.remove(path)
    print("[+] Removed script: {}".format(path))


def parse_args():
    parser = argparse.ArgumentParser(description="Unregisters the given commands")
    parser.add_argument("names", help="The scripts to unregister", nargs="+")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    for name in args.names:
        unregister(name)


if __name__ == '__main__':
    main()
