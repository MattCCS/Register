
import os
import pathlib

TARGET = pathlib.Path("/usr/local/bin/registered")
if not TARGET.exists():
    os.mkdir(TARGET)
assert TARGET.exists()
