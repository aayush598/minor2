import cv2
import os
import numpy as np
import basic_operations

# Define the output directory
output_dir = "results/basic_operations"

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

# Apply basic operations
operations = {
    "negation": basic_operations.image_negation(img),
    "threshold": basic_operations.threshold(img, threshold_value=128),
    "brightness_adjusted": basic_operations.brightness_adjust(img, factor=1.2),
    "contrast_adjusted": basic_operations.contrast_adjust(img, factor=1.2),
    "gamma_corrected": basic_operations.gamma_correction(img, gamma=1.5),
    "log_transformed": basic_operations.log_transform(img),
    "inverse_log_transformed": basic_operations.inverse_log_transform(img),
}

# Apply bit-plane slicing (0-7 bit planes)
for i in range(8):
    operations[f"bit_plane_{i}"] = basic_operations.bit_plane_slicing(img, bit_plane=i)

# Save processed images
for name, processed_img in operations.items():
    output_path = os.path.join(output_dir, f"{name}.png")
    cv2.imwrite(output_path, processed_img)
    print(f"Saved: {output_path}")

print("All basic operations completed and saved in 'results/basic_operations/' folder.")
