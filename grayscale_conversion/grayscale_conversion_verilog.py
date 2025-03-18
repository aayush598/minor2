import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input image
image = cv2.imread("input_image.png")  # Read as BGR format

# Convert BGR to RGB (since OpenCV loads images in BGR order)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Extract R, G, B channels
R = image_rgb[:, :, 0].astype(np.uint16)  # Convert to uint16 to avoid overflow
G = image_rgb[:, :, 1].astype(np.uint16)
B = image_rgb[:, :, 2].astype(np.uint16)

# Verilog-friendly grayscale conversion (fixed-point approximation)
grayscale = (77 * R + 150 * G + 29 * B) >> 8  # Equivalent to / 256

# Convert to uint8 (0-255 range)
grayscale = grayscale.astype(np.uint8)

# Save grayscale image
cv2.imwrite("grayscale_output.png", grayscale)

# Save grayscale pixel values as a HEX file (for Verilog memory)
with open("grayscale_values.hex", "w") as f:
    for row in grayscale:
        hex_values = ' '.join(f"{val:02X}" for val in row)
        f.write(hex_values + "\n")

# Print sample values (for Verilog testbench comparison)
print("Sample RGB and Grayscale Values:")
for i in range(5):  # Print first 5 pixels from the top-left corner
    r, g, b = R[0, i], G[0, i], B[0, i]
    gray = grayscale[0, i]
    print(f"RGB({r:02X}, {g:02X}, {b:02X}) -> Gray({gray:02X})")

# Display the original and grayscale images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(grayscale, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

plt.show()
