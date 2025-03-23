import cv2
import os
import numpy as np
import filtering_smoothing

# Define the output directory
output_dir = "results/filterSmoothing"

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

# Apply filtering and smoothing operations
operations = {
    "mean_filter": filtering_smoothing.mean_filter(img, kernel_size=3),
    "median_filter": filtering_smoothing.median_filter(img, kernel_size=3),
    "gaussian_filter": filtering_smoothing.gaussian_filter(img, kernel_size=3, sigma=1.0),
    "sharpening_filter": filtering_smoothing.sharpening_filter(img),
}

# Save processed images
for name, processed_img in operations.items():
    output_path = os.path.join(output_dir, f"{name}.png")
    cv2.imwrite(output_path, processed_img)
    print(f"Saved: {output_path}")

print("All filtering & smoothing operations completed and saved in 'results/filterSmoothing/' folder.")
