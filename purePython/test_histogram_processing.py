import cv2
import os
import numpy as np
import histogram_processing

# Define the output directory
output_dir = "results/histogram_processing"

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

# Load the input image (grayscale)
input_image_path = "images/sample.png"  # Change this to your input image path
img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Unable to load image at {input_image_path}")
    exit()

# Apply histogram-based processing techniques
operations = {
    "original": img,
    "equalized": histogram_processing.histogram_equalization(img),
    "normalized": histogram_processing.normalize_histogram(img),
    "otsu_threshold": histogram_processing.threshold_otsu(img),
}

# Save processed images
for name, processed_img in operations.items():
    output_path = os.path.join(output_dir, f"{name}.png")
    cv2.imwrite(output_path, processed_img)
    print(f"Saved: {output_path}")

print("All histogram-based processing operations completed and saved in 'results/histogram_processing/' folder.")
