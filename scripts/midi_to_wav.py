#!/usr/bin/env python3

from pathlib import Path
from sys import argv
import subprocess
import shlex

# Takes in a directory and converts all midi files to .wav

def convert_all_midi_to_wav(folder_path):
    files = [file for file in folder_path.iterdir() if file.is_file() and ("mid" in file.name)]
    for (x, file) in enumerate(files):
        without_file_extension = file.name[:-4]
        resolved = Path(f'{folder_path}/{without_file_extension}')
        # synth adds .mid to input file by default, so we remove it first
        if (Path(f'{resolved}.wav').is_file() == False):
            # Check if .wav exists, so we can safely re-run the file without re-converting
            # any files that were already converted
            print('Converting...', without_file_extension)
            subprocess.call(shlex.split(f'./convert_midi_to_wav.sh {resolved}'))


def do_recursively_on_folders(dir_path, action):
    folders = [folder for folder in dir_path.iterdir() if folder.is_dir()]
    for folder in folders:
        action(folder)

path = Path(argv[1])
do_recursively_on_folders(path, convert_all_midi_to_wav)
