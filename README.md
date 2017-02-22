Register
========
A simple command-line tool to manage and collect custom scripts (by symlink).

Requirements
------------
- Requires the directory `/usr/local/bin/registered`
- Python 3+
- Bash

How to Use
----------
Scripts are found in the `scripts` directory.

Run `register` to see a list of registered scripts (starts as empty).

Run `register <script path>` to register a script.  You will be prompted for an *optional* name change.

Run `unregister <command name>` to unregister a script.  You must pass a name that's been registered (i.e., a name that appears when you run `register`).

Pro Tips
--------
Run `register scripts/register` and `register scripts/unregister`!  That's sort of the point, after all.  ;)
