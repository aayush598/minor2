import numpy as np

def compute_histogram(img):
    """ Compute the histogram of an image """
    hist = np.zeros(256, dtype=int)
    for pixel_value in img.flatten():
        hist[pixel_value] += 1
    return hist

def histogram_equalization(img):
    """ Perform histogram equalization """
    hist = compute_histogram(img)
    cdf = np.cumsum(hist)  # Cumulative distribution function
    cdf_min = cdf[np.nonzero(cdf)][0]  # First nonzero element in CDF
    total_pixels = img.size

    # Compute equalized values
    equalized_values = np.round(((cdf - cdf_min) / (total_pixels - cdf_min)) * 255).astype(np.uint8)

    # Apply new pixel values
    equalized_img = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            equalized_img[i, j] = equalized_values[img[i, j]]

    return equalized_img

def normalize_histogram(img):
    """ Normalize histogram to enhance contrast """
    min_val, max_val = np.min(img), np.max(img)
    normalized_img = ((img - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return normalized_img

def threshold_otsu(img):
    """ Compute Otsu's thresholding """
    hist = compute_histogram(img)
    total_pixels = img.size
    sum_total = np.sum(np.arange(256) * hist)

    sum_background, weight_background, max_variance, best_threshold = 0, 0, 0, 0
    weight_foreground = total_pixels

    for threshold in range(256):
        weight_background += hist[threshold]
        weight_foreground -= hist[threshold]

        if weight_background == 0 or weight_foreground == 0:
            continue

        sum_background += threshold * hist[threshold]
        mean_background = sum_background / weight_background
        mean_foreground = (sum_total - sum_background) / weight_foreground

        variance_between = weight_background * weight_foreground * (mean_background - mean_foreground) ** 2

        if variance_between > max_variance:
            max_variance = variance_between
            best_threshold = threshold

    return np.where(img > best_threshold, 255, 0).astype(np.uint8)

