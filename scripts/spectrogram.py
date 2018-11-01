#!/usr/bin/env python3

from pathlib import Path
from sys import argv
from scipy import signal
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

def create_spectrograms(folder_path):
    files = [file for file in folder_path.iterdir() if file.is_file() and ("wav" in file.name)]
    for (x, file) in enumerate(files):
        without_file_extension = file.name[:-4]
        resolved = Path(f'{folder_path}/{without_file_extension}')
        if (Path(f'{resolved}.png').is_file() == False):
            print('making spectro for', resolved)
            sample_rate, samples = wavfile.read(file)
            frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
            plt.pcolormesh(np.log(spectrogram))
            plt.axis('off')
            plt.ylim(ymax=40)
            # plt.show() # Uncomment if you want to check out the plot.
            plt.savefig(f'{resolved}.png', transparent=True)
            # saves the file as a .png with transparent background (no border)

def do_recursively_on_folders(dir_path, action):
    folders = [folder for folder in dir_path.iterdir() if folder.is_dir()]
    for folder in folders:
        action(folder)
    print('FINISHED PROCESSING! :-)')

if (len(argv) < 2):
    raise Exception('Please specify a path')
path = Path(argv[1])
do_recursively_on_folders(path, create_spectrograms)
