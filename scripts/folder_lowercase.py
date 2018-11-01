#!/usr/bin/env python3

from pathlib import Path
from sys import argv

# Downcases a the names of all directories inside the current directory.

path = Path('.')
dirs = [file for file in path.iterdir() if file.is_dir()]
for (x, dir) in enumerate(dirs):
    print('Changing', dir)
    dir.rename(dir.name.lower())
print('Done')
