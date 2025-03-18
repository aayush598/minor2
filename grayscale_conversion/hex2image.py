import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load HEX file
hex_file = "grayscale_values.hex"

# Read HEX values and convert back to grayscale
grayscale_values = []
with open(hex_file, "r") as f:
    for line in f:
        hex_numbers = line.strip().split()  # Split HEX values
        grayscale_values.extend(int(x, 16) for x in hex_numbers)  # Convert HEX to int

# Determine image dimensions
original_image = cv2.imread("input_image.png", cv2.IMREAD_GRAYSCALE)  # Load original to get dimensions
height, width = original_image.shape

# Reshape into image format
grayscale_image = np.array(grayscale_values, dtype=np.uint8).reshape((height, width))

# Save the reconstructed image
cv2.imwrite("reconstructed_image.png", grayscale_image)

# Display the reconstructed image
plt.imshow(grayscale_image, cmap="gray")
plt.title("Reconstructed Grayscale Image")
plt.axis("off")
plt.show()

print("Image successfully reconstructed and saved as 'reconstructed_image.png'.")
