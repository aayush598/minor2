import cv2
import os
import numpy as np
import morphological_operations

# Define the output directory
output_dir = "results/morphological"

# Ensure results directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
else:
    # Delete all existing files in the folder
    for file in os.listdir(output_dir):
        file_path = os.path.join(output_dir, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print(f"Deleted all existing images in '{output_dir}'")

# Load the input image (binary image)
input_image_path = "images/sample.png"  # Change this to your input image path
img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Unable to load image at {input_image_path}")
    exit()

# Convert to binary (thresholding)
_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Apply morphological operations
operations = {
    "dilation": morphological_operations.dilation(binary_img, 3),
    "erosion": morphological_operations.erosion(binary_img, 3),
    "opening": morphological_operations.opening(binary_img, 3),
    "closing": morphological_operations.closing(binary_img, 3),
    "boundary_extraction": morphological_operations.boundary_extraction(binary_img, 3),
}

# Save processed images
for name, processed_img in operations.items():
    output_path = os.path.join(output_dir, f"{name}.png")
    cv2.imwrite(output_path, processed_img)
    print(f"Saved: {output_path}")

print("All morphological operations completed and saved in 'results/morphological/' folder.")
