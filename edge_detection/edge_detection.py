import cv2
import numpy as np

# Load grayscale image
image = cv2.imread("input_image.png", cv2.IMREAD_GRAYSCALE).astype(np.uint16)

# Sobel Kernels (Fixed-Point Integer)
sobel_x = np.array([[-1,  0,  1], 
                     [-2,  0,  2], 
                     [-1,  0,  1]], dtype=np.int16)

sobel_y = np.array([[-1, -2, -1], 
                     [ 0,  0,  0], 
                     [ 1,  2,  1]], dtype=np.int16)

# Get image dimensions
height, width = image.shape
edge_image = np.zeros((height, width), dtype=np.uint8)

# Apply convolution (Manual Calculation)
for y in range(1, height - 1):
    for x in range(1, width - 1):
        Gx = np.sum(image[y - 1:y + 2, x - 1:x + 2] * sobel_x)
        Gy = np.sum(image[y - 1:y + 2, x - 1:x + 2] * sobel_y)
        
        # Compute edge magnitude (Approximation for Verilog: |Gx| + |Gy|)
        edge_value = min(abs(Gx) + abs(Gy), 255)  # Clip to 8-bit range
        
        edge_image[y, x] = edge_value  # Store result

# Save edge-detected image
cv2.imwrite("edge_output.png", edge_image)
