import numpy as np

def translate(img, tx, ty):
    """ Perform translation transformation """
    h, w = img.shape
    translated_img = np.zeros_like(img)

    for i in range(h):
        for j in range(w):
            new_x = j + tx
            new_y = i + ty
            if 0 <= new_x < w and 0 <= new_y < h:
                translated_img[new_y, new_x] = img[i, j]
    
    return translated_img

def scale(img, sx, sy):
    """ Perform scaling transformation """
    h, w = img.shape
    new_h, new_w = int(h * sy), int(w * sx)
    scaled_img = np.zeros((new_h, new_w), dtype=np.uint8)

    for i in range(new_h):
        for j in range(new_w):
            orig_x = int(j / sx)
            orig_y = int(i / sy)
            if orig_x < w and orig_y < h:
                scaled_img[i, j] = img[orig_y, orig_x]

    return scaled_img

def rotate(img, angle):
    """ Perform rotation transformation """
    h, w = img.shape
    angle_rad = np.radians(angle)
    cos_a = np.cos(angle_rad)
    sin_a = np.sin(angle_rad)
    new_h, new_w = h, w  # Keeping size same to prevent cropping

    rotated_img = np.zeros_like(img)
    center_x, center_y = w // 2, h // 2

    for i in range(h):
        for j in range(w):
            x = j - center_x
            y = i - center_y
            new_x = int(center_x + x * cos_a - y * sin_a)
            new_y = int(center_y + x * sin_a + y * cos_a)

            if 0 <= new_x < w and 0 <= new_y < h:
                rotated_img[new_y, new_x] = img[i, j]

    return rotated_img

def flip_horizontal(img):
    """ Perform horizontal flipping """
    return img[:, ::-1]

def flip_vertical(img):
    """ Perform vertical flipping """
    return img[::-1, :]

def shear(img, shx, shy):
    """ Perform shearing transformation """
    h, w = img.shape
    new_w = int(w + h * abs(shx))
    new_h = int(h + w * abs(shy))
    sheared_img = np.zeros((new_h, new_w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            new_x = j + int(i * shx)
            new_y = i + int(j * shy)
            if 0 <= new_x < new_w and 0 <= new_y < new_h:
                sheared_img[new_y, new_x] = img[i, j]

    return sheared_img
