import cv2
import os
import numpy as np
import edge_detection

# Define the output directory
output_dir = "results/edgeDetection"

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

# Load the input image (grayscale mode)
input_image_path = "images/sample.png"  # Change this to your input image path
img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Unable to load image at {input_image_path}")
    exit()

# Apply edge detection operations
operations = {
    "sobel_operator": edge_detection.sobel_operator(img),
    "prewitt_operator": edge_detection.prewitt_operator(img),
    "roberts_operator": edge_detection.roberts_operator(img),
    "laplacian_operator": edge_detection.laplacian_operator(img),
}

# Save processed images
for name, processed_img in operations.items():
    output_path = os.path.join(output_dir, f"{name}.png")
    cv2.imwrite(output_path, processed_img)
    print(f"Saved: {output_path}")

print("All edge detection operations completed and saved in 'results/edgeDetection/' folder.")
