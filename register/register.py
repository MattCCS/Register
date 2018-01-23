"""
Register the given script in /usr/local/bin/registered
"""

import argparse
import os
import pathlib
import subprocess

from register import settings


def show_with_help():
    print("Registered Commands:")
    print("--------------------")
    commands = subprocess.check_output(['ls', settings.TARGET]).decode('utf-8').strip().split()
    commands = [(cmd, os.path.realpath(settings.TARGET / cmd)) for cmd in commands]
    for (cmd, src) in sorted(commands, key=lambda p: (p[1], len(p[0]))):
        print("{:<13} -> {}".format(cmd, src))
    print()


def add(pwd, script):
    pwd = pathlib.Path(pwd)
    script = pathlib.Path(script)
    if not script.is_absolute():
        script = pathlib.Path(os.path.normpath(pwd / script))

    if not script.exists():
        print("[-] Path does not exist: {}".format(script))
        return

    name = input("[ ] Choose a name for {} (ENTER to pass): ".format(script))
    target = settings.TARGET
    if not name:
        name = script.name
    target = target / name

    if target.exists():
        print("[-] Target already exists: {}".format(target))
        return

    os.symlink(script, target)
    print("[+] Registered {} as {}.\n".format(script, target.name))


def parse_args():
    parser = argparse.ArgumentParser(description="Registers the given commands, or lists registered commands")
    parser.add_argument("pwd", help=argparse.SUPPRESS)
    parser.add_argument("scripts", help="The scripts to register", nargs="*")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if not args.scripts:
        return show_with_help()

    for script in args.scripts:
        add(args.pwd, script)


if __name__ == '__main__':
    main()
