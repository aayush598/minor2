import numpy as np

def dilation(img, kernel_size=3):
    """ Perform Dilation on a binary image """
    pad = kernel_size // 2
    img_padded = np.pad(img, pad, mode='constant', constant_values=0)
    output_img = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = img_padded[i:i+kernel_size, j:j+kernel_size]
            output_img[i, j] = np.max(region)  # Max value in the neighborhood

    return output_img

def erosion(img, kernel_size=3):
    """ Perform Erosion on a binary image """
    pad = kernel_size // 2
    img_padded = np.pad(img, pad, mode='constant', constant_values=0)
    output_img = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = img_padded[i:i+kernel_size, j:j+kernel_size]
            output_img[i, j] = np.min(region)  # Min value in the neighborhood

    return output_img

def opening(img, kernel_size=3):
    """ Perform Opening (Erosion followed by Dilation) """
    eroded_img = erosion(img, kernel_size)
    opened_img = dilation(eroded_img, kernel_size)
    return opened_img

def closing(img, kernel_size=3):
    """ Perform Closing (Dilation followed by Erosion) """
    dilated_img = dilation(img, kernel_size)
    closed_img = erosion(dilated_img, kernel_size)
    return closed_img

def boundary_extraction(img, kernel_size=3):
    """ Extract boundary using Morphological Operations """
    eroded_img = erosion(img, kernel_size)
    boundary = img - eroded_img
    return boundary
