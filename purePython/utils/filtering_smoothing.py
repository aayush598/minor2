import numpy as np

def mean_filter(img, kernel_size=3):
    """ Apply Mean Filter (Averaging Filter) """
    pad = kernel_size // 2
    img_padded = np.pad(img, pad, mode='constant', constant_values=0)
    filtered_img = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            filtered_img[i, j] = np.mean(img_padded[i:i+kernel_size, j:j+kernel_size])

    return filtered_img.astype(np.uint8)

def median_filter(img, kernel_size=3):
    """ Apply Median Filter """
    pad = kernel_size // 2
    img_padded = np.pad(img, pad, mode='constant', constant_values=0)
    filtered_img = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            filtered_img[i, j] = np.median(img_padded[i:i+kernel_size, j:j+kernel_size])

    return filtered_img.astype(np.uint8)

def gaussian_filter(img, kernel_size=3, sigma=1.0):
    """ Apply Gaussian Filter (Supports both Grayscale and RGB images) """
    if len(img.shape) == 3:  # RGB Image
        return np.dstack([gaussian_filter(img[:, :, i], kernel_size, sigma) for i in range(img.shape[2])])

    pad = kernel_size // 2
    x, y = np.mgrid[-pad:pad+1, -pad:pad+1]
    gaussian_kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    gaussian_kernel /= gaussian_kernel.sum()

    img_padded = np.pad(img, pad, mode='constant', constant_values=0)
    filtered_img = np.zeros_like(img, dtype=np.float32)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            filtered_img[i, j] = np.sum(img_padded[i:i+kernel_size, j:j+kernel_size] * gaussian_kernel)

    return np.clip(filtered_img, 0, 255).astype(np.uint8)

def sharpening_filter(img):
    """ Apply Sharpening Filter (Supports both Grayscale and RGB images) """
    kernel = np.array([[ 0, -1,  0],
                       [-1,  5, -1],
                       [ 0, -1,  0]])
    
    if len(img.shape) == 3:  # If RGB image, apply filter to each channel separately
        return np.dstack([sharpening_filter(img[:, :, i]) for i in range(img.shape[2])])

    pad = 1
    img_padded = np.pad(img, pad, mode='constant', constant_values=0)
    filtered_img = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            filtered_img[i, j] = np.sum(img_padded[i:i+3, j:j+3] * kernel)

    return np.clip(filtered_img, 0, 255).astype(np.uint8)
