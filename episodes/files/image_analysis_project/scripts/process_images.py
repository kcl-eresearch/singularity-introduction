#!/usr/bin/env python

# Usage: python process_images.py path/to/dir
# Processes all files in directory by extracting first channel and saving as a numpy array

import os
import sys
import numpy as np
from skimage import io

def process_image(input_file):
    im_read = io.imread(input_file)
    
    # rearrange channels to (c, x, y)
    im_all = np.transpose(im_read, (2, 0, 1))

    # select the channel containing the nuclei
    im = im_all[0,]

    # save processed image
    file_name, ext = os.path.splitext(input_file)
    file_name = file_name + '_processed.npy'

    np.save(file_name, im)


if __name__ == "__main__":
    input_dir = sys.argv[1]

    # list all files in input directory
    files = os.listdir(input_dir)

    for f in files:
        process_image(os.path.join(input_dir, f))
