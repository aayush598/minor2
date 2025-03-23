import cv2
import os
import numpy as np
import geometric_transformations

# Define the output directory
output_dir = "results/geometric_transformations"

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

# Apply geometric transformations
operations = {
    "translated": geometric_transformations.translate(img, tx=50, ty=30),
    "scaled": geometric_transformations.scale(img, sx=1.5, sy=1.5),
    "rotated": geometric_transformations.rotate(img, angle=45),
    "flipped_horizontal": geometric_transformations.flip_horizontal(img),
    "flipped_vertical": geometric_transformations.flip_vertical(img),
    "sheared": geometric_transformations.shear(img, shx=0.3, shy=0.2),
}

# Save processed images
for name, processed_img in operations.items():
    output_path = os.path.join(output_dir, f"{name}.png")
    cv2.imwrite(output_path, processed_img)
    print(f"Saved: {output_path}")

print("All geometric transformations completed and saved in 'results/geometric_transformations/' folder.")
