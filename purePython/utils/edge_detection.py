import numpy as np

def sobel_operator(img):
    """ Apply Sobel Edge Detection (Gradient Calculation) """
    Gx = np.array([[-1, 0, 1], 
                   [-2, 0, 2], 
                   [-1, 0, 1]])

    Gy = np.array([[-1, -2, -1], 
                   [ 0,  0,  0], 
                   [ 1,  2,  1]])

    pad = 1
    img_padded = np.pad(img, pad, mode='constant', constant_values=0)
    gradient_img = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            gx = np.sum(img_padded[i:i+3, j:j+3] * Gx)
            gy = np.sum(img_padded[i:i+3, j:j+3] * Gy)
            gradient_img[i, j] = np.sqrt(gx**2 + gy**2)

    return np.clip(gradient_img, 0, 255).astype(np.uint8)

def prewitt_operator(img):
    """ Apply Prewitt Edge Detection """
    Gx = np.array([[-1, 0, 1], 
                   [-1, 0, 1], 
                   [-1, 0, 1]])

    Gy = np.array([[-1, -1, -1], 
                   [ 0,  0,  0], 
                   [ 1,  1,  1]])

    pad = 1
    img_padded = np.pad(img, pad, mode='constant', constant_values=0)
    gradient_img = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            gx = np.sum(img_padded[i:i+3, j:j+3] * Gx)
            gy = np.sum(img_padded[i:i+3, j:j+3] * Gy)
            gradient_img[i, j] = np.sqrt(gx**2 + gy**2)

    return np.clip(gradient_img, 0, 255).astype(np.uint8)

def roberts_operator(img):
    """ Apply Roberts Cross Edge Detection """
    Gx = np.array([[ 1, 0], 
                   [ 0, -1]])

    Gy = np.array([[ 0, 1], 
                   [-1,  0]])

    img_padded = np.pad(img, 1, mode='constant', constant_values=0)
    gradient_img = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            gx = np.sum(img_padded[i:i+2, j:j+2] * Gx)
            gy = np.sum(img_padded[i:i+2, j:j+2] * Gy)
            gradient_img[i, j] = np.sqrt(gx**2 + gy**2)

    return np.clip(gradient_img, 0, 255).astype(np.uint8)

def laplacian_operator(img):
    """ Apply Laplacian Edge Detection """
    kernel = np.array([[ 0,  1,  0], 
                       [ 1, -4,  1], 
                       [ 0,  1,  0]])

    pad = 1
    img_padded = np.pad(img, pad, mode='constant', constant_values=0)
    gradient_img = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            gradient_img[i, j] = np.sum(img_padded[i:i+3, j:j+3] * kernel)

    return np.clip(gradient_img, 0, 255).astype(np.uint8)
