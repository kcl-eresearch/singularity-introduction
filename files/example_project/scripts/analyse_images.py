#!/usr/bin/env python

# Usage: python analyse_images.py path/to/dir
# Reads all .npy files in directory, detects blobs, and outputs blob stats to a csv file

import os
import sys
import numpy as np
import pandas as pd
from skimage import filters
from skimage import measure
import matplotlib.pyplot as plt


def analyse_image(input_file):
    processed_image = np.load(input_file)

    # Gaussian blur (sigma=5)
    im_gauss = filters.gaussian(processed_image, sigma=5)
    
    # segment image using Otsu method
    thresh = filters.threshold_otsu(im_gauss)
    im_thresh = im_gauss >= thresh
    labels = measure.label(im_thresh)
    
    # count the objects - find the maximum integer assigned to a label!
    print('There are', labels.max(), 'objects in the image')
    
    # measure properties
    props = measure.regionprops_table(labels, processed_image, properties=['area', 'centroid', 'eccentricity'])
    props_df = pd.DataFrame(props)
    props_df['blob_id'] = props_df.index + 1

    # plot segmented image
    im_segmented = processed_image * im_thresh
    
    fig, ax = plt.subplots(figsize=(8,6))
    ax.imshow(im_segmented, cmap='gray')
    ax.axis('off')
    plt.tight_layout()
    
    # plot centroids
    plt.plot(props_df['centroid-1'], props_df['centroid-0'], 'co')
    filename, ext = os.path.splitext(input_file)
    fig.savefig(filename + "_blob_centroids.png")

    return(props_df)


if __name__ == "__main__":
    input_dir = sys.argv[1]

    # list all .npy files in input directory
    files = os.listdir(input_dir)
    files = [f for f in files if f.endswith("npy")]

    props_df = pd.DataFrame()
    
    for f in files:
        # analyse one image
        props_tmp = analyse_image(os.path.join(input_dir, f))
        props_tmp['image_ID'] = f

        # add to output dataframe
        props_df = pd.concat([props_df, props_tmp], ignore_index=True)

    props_df.to_csv(os.path.join(input_dir, "all_image_stats.csv"))

