#!/usr/bin/env python3

from pathlib import Path
from sys import argv

# Recursive Renaming!
# Converts all files in specified directory to format [foldername]_[filenumber]
def rename_files(folder_path, folder_name):
    files = [file for file in folder_path.iterdir() if file.is_file() and ("mid" in file.name)]
    for (x, file) in enumerate(files):
        print('Renaming', file)
        file.rename(f'{folder_path}/{folder_name}_{x}.mid')
    print('Done')

def recursive_rename(dir_path):
    folders = [folder for folder in dir_path.iterdir() if folder.is_dir()]
    for folder in folders:
        print('Renaming:', folder.name)
        rename_files(root_path/f'{folder.name}', folder.name)

if (len(argv) < 2):
    raise Exception('Please specify a path')
path = Path(argv[1])
recursive_rename(root_path)
