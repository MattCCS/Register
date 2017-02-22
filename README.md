Register
========

A simple command-line tool to manage and collect custom scripts (by symlink).

Requirements
------------

You must create the directory `/usr/local/bin/registered`.

How to Use
----------
Run `register` to see a list of registered scripts (starts as empty).

Run `register <script path>` to register a script.  You will be prompted for an optional name change.

Run `unregister <command name>` to unregister a script.  You must pass a name that's been registered/that appears when you run `register`.
