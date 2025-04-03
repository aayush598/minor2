import cv2
import os
import numpy as np
from utils import basic_operations, edge_detection, filtering_smoothing, geometric_transformations, histogram_processing, morphological_operations

# Define test categories and their respective output folders
test_categories = {
    "basic_operations": basic_operations,
    "edgeDetection": edge_detection,
    "filterSmoothing": filtering_smoothing,
    "geometric_transformations": geometric_transformations,
    "histogram_processing": histogram_processing,
    "morphological": morphological_operations
}

# Ensure results directories exist and clear previous results
for category in test_categories.keys():
    output_dir = f"results/{category}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        for file in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print(f"Deleted all existing images in '{output_dir}'")

# Load the input image (RGB mode)
input_image_path = "images/sample.png"  # Change this to your input image path
img = cv2.imread(input_image_path, cv2.IMREAD_COLOR)

if img is None:
    print(f"Error: Unable to load image at {input_image_path}")
    exit()

# Convert RGB to Grayscale for operations requiring binary images
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)

# Define operations for each category
operations = {
    "basic_operations": {
        "negation": basic_operations.image_negation(img),
        "threshold": basic_operations.threshold(img, threshold_value=128),
        "brightness_adjusted": basic_operations.brightness_adjust(img, factor=1.2),
        "contrast_adjusted": basic_operations.contrast_adjust(img, factor=1.2),
        "gamma_corrected": basic_operations.gamma_correction(img, gamma=1.5),
        "log_transformed": basic_operations.log_transform(img),
        "inverse_log_transformed": basic_operations.inverse_log_transform(img),
        **{f"bit_plane_{i}": basic_operations.bit_plane_slicing(img, bit_plane=i) for i in range(8)}
    },
    "edgeDetection": {
        "sobel_operator": edge_detection.sobel_operator(gray_img),
        "prewitt_operator": edge_detection.prewitt_operator(gray_img),
        "roberts_operator": edge_detection.roberts_operator(gray_img),
        "laplacian_operator": edge_detection.laplacian_operator(gray_img),
    },
    "filterSmoothing": {
        "mean_filter": filtering_smoothing.mean_filter(img, kernel_size=3),
        "median_filter": filtering_smoothing.median_filter(img, kernel_size=3),
        "gaussian_filter": filtering_smoothing.gaussian_filter(img, kernel_size=3, sigma=1.0),
        "sharpening_filter": filtering_smoothing.sharpening_filter(img),
    },
    "geometric_transformations": {
        "translated": geometric_transformations.translate(img, tx=50, ty=30),
        "scaled": geometric_transformations.scale(img, sx=1.5, sy=1.5),
        "rotated": geometric_transformations.rotate(img, angle=45),
        "flipped_horizontal": geometric_transformations.flip_horizontal(img),
        "flipped_vertical": geometric_transformations.flip_vertical(img),
        "sheared": geometric_transformations.shear(img, shx=0.3, shy=0.2),
    },
    "histogram_processing": {
        "original": img,
        "equalized": histogram_processing.histogram_equalization(img),
        "normalized": histogram_processing.normalize_histogram(img),
        "otsu_threshold": histogram_processing.threshold_otsu(img),
    },
    "morphological": {
        "dilation": morphological_operations.dilation(binary_img, 3),
        "erosion": morphological_operations.erosion(binary_img, 3),
        "opening": morphological_operations.opening(binary_img, 3),
        "closing": morphological_operations.closing(binary_img, 3),
        "boundary_extraction": morphological_operations.boundary_extraction(binary_img, 3),
    }
}

# Process and save all images
for category, ops in operations.items():
    output_dir = f"results/{category}"
    for name, processed_img in ops.items():
        output_path = os.path.join(output_dir, f"{name}.png")
        cv2.imwrite(output_path, processed_img)
        print(f"Saved: {output_path}")

print("✅ All image processing operations completed successfully!")
