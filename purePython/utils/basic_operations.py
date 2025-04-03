import numpy as np

def image_negation(img):
    """ Perform image negation """
    return 255 - img

def threshold(img, threshold_value=128):
    """ Apply thresholding """
    return np.where(img > threshold_value, 255, 0).astype(np.uint8)

def brightness_adjust(img, factor=1.2):
    """ Adjust brightness by multiplying pixel values with a factor """
    return np.clip(img * factor, 0, 255).astype(np.uint8)

def contrast_adjust(img, factor=1.2):
    """ Adjust contrast by scaling pixel values """
    mean = np.mean(img)
    return np.clip((img - mean) * factor + mean, 0, 255).astype(np.uint8)

def gamma_correction(img, gamma=1.0):
    """ Apply gamma correction """
    inv_gamma = 1.0 / gamma
    return np.clip(255 * (img / 255) ** inv_gamma, 0, 255).astype(np.uint8)

def log_transform(img):
    """ Apply logarithmic transformation """
    img = img.astype(np.float32)  # Ensure it's float for log calculation
    max_val = np.max(img)
    if max_val == 0:
        max_val = 1  # Avoid division by zero

    c = 255 / np.log(1 + max_val)
    return np.clip(c * np.log(1 + img), 0, 255).astype(np.uint8)

def inverse_log_transform(img):
    """ Apply inverse logarithmic transformation """
    img = img.astype(np.float32)
    max_val = np.max(img)
    if max_val == 0:
        max_val = 1  # Avoid division by zero

    c = 255 / np.log(1 + max_val)
    return np.clip(np.exp(img / c) - 1, 0, 255).astype(np.uint8)

def bit_plane_slicing(img, bit_plane=0):
    """ Extract a specific bit plane """
    return ((img >> bit_plane) & 1) * 255
