import numpy as np

def translate(img, tx, ty):
    """ Perform translation transformation (Supports Grayscale and RGB) """
    if len(img.shape) == 3:  # RGB Image
        h, w, c = img.shape
        translated_img = np.zeros_like(img)
        for ch in range(c):
            for i in range(h):
                for j in range(w):
                    new_x = j + tx
                    new_y = i + ty
                    if 0 <= new_x < w and 0 <= new_y < h:
                        translated_img[new_y, new_x, ch] = img[i, j, ch]
    else:  # Grayscale Image
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
    """ Perform scaling transformation (Supports Grayscale and RGB) """
    if len(img.shape) == 3:  # RGB Image
        h, w, c = img.shape
        new_h, new_w = int(h * sy), int(w * sx)
        scaled_img = np.zeros((new_h, new_w, c), dtype=np.uint8)

        for ch in range(c):
            for i in range(new_h):
                for j in range(new_w):
                    orig_x = int(j / sx)
                    orig_y = int(i / sy)
                    if orig_x < w and orig_y < h:
                        scaled_img[i, j, ch] = img[orig_y, orig_x, ch]
    else:  # Grayscale Image
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
    """ Perform rotation transformation (Supports Grayscale and RGB) """
    angle_rad = np.radians(angle)
    cos_a, sin_a = np.cos(angle_rad), np.sin(angle_rad)

    if len(img.shape) == 3:  # RGB Image
        h, w, c = img.shape
        rotated_img = np.zeros_like(img)
    else:  # Grayscale Image
        h, w = img.shape
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
    """ Perform horizontal flipping (Supports Grayscale and RGB) """
    return img[:, ::-1, :] if len(img.shape) == 3 else img[:, ::-1]


def flip_vertical(img):
    """ Perform vertical flipping (Supports Grayscale and RGB) """
    return img[::-1, :, :] if len(img.shape) == 3 else img[::-1, :]


def shear(img, shx, shy):
    """ Perform shearing transformation (Supports Grayscale and RGB) """
    if len(img.shape) == 3:  # RGB Image
        h, w, c = img.shape
        new_w = int(w + h * abs(shx))
        new_h = int(h + w * abs(shy))
        sheared_img = np.zeros((new_h, new_w, c), dtype=np.uint8)

        for ch in range(c):
            for i in range(h):
                for j in range(w):
                    new_x = j + int(i * shx)
                    new_y = i + int(j * shy)
                    if 0 <= new_x < new_w and 0 <= new_y < new_h:
                        sheared_img[new_y, new_x, ch] = img[i, j, ch]
    else:  # Grayscale Image
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
