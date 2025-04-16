import streamlit as st
import os
from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import numpy as np

# Operation to 4-bit binary mapping
operation_map = {
    "brightness": "0000",
    "contrast": "0001",
    "negation": "0010",
    "edge detection": "0011",
    "smoothing": "0100",
    "sharpening": "0101",
    "gaussian": "0110",
    "translate": "0111",
    "scale": "1000",
    "rotate": "1001",
    "flip horizontal": "1010",
    "flip vertical": "1011",
    "sheared": "1100",
    "grayscale": "1101",
    "compression": "1110",
    "morphological": "1111"
}

# Ensure folders exist
os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

st.title("🧊 Image Operation to Hex File (RGB)")

# Upload an image
uploaded_file = st.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg", "bmp"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Original Image", use_column_width=True)

    # Operation selection
    operation = st.selectbox("🎯 Choose an operation", list(operation_map.keys()))
    binary_code = operation_map[operation]
    st.markdown(f"🔢 **4-bit binary code for `{operation}`: `{binary_code}`**")

    # Apply operation
    def apply_operation(img, op):
        if op == "brightness":
            return ImageEnhance.Brightness(img).enhance(1.5)
        elif op == "contrast":
            return ImageEnhance.Contrast(img).enhance(1.5)
        elif op == "negation":
            return ImageOps.invert(img)
        elif op == "edge detection":
            return img.filter(ImageFilter.FIND_EDGES)
        elif op == "smoothing":
            return img.filter(ImageFilter.SMOOTH)
        elif op == "sharpening":
            return img.filter(ImageFilter.SHARPEN)
        elif op == "gaussian":
            return img.filter(ImageFilter.GaussianBlur(radius=2))
        elif op == "translate":
            return img.transform(img.size, Image.AFFINE, (1, 0, 20, 0, 1, 20))
        elif op == "scale":
            return img.resize((img.size[0] * 2, img.size[1] * 2))
        elif op == "rotate":
            return img.rotate(45)
        elif op == "flip horizontal":
            return img.transpose(Image.FLIP_LEFT_RIGHT)
        elif op == "flip vertical":
            return img.transpose(Image.FLIP_TOP_BOTTOM)
        elif op == "sheared":
            return img.transform(img.size, Image.AFFINE, (1, 0.5, 0, 0.5, 1, 0))
        elif op == "grayscale":
            return img.convert("L").convert("RGB")
        elif op == "compression":
            temp_path = "temp_compressed.jpg"
            img.save(temp_path, "JPEG", quality=10)
            return Image.open(temp_path).convert("RGB")
        elif op == "morphological":
            return img.filter(ImageFilter.MinFilter(3))
        return img

    processed_image = apply_operation(image, operation)

    # Convert processed image to RGB hex string
    pixels = list(processed_image.getdata())
    hex_data = ''.join([f"{r:02x}{g:02x}{b:02x}" for r, g, b in pixels])

    # Save hex to file
    base_filename = os.path.splitext(uploaded_file.name)[0]
    output_file_path = os.path.join("output", f"{base_filename}_{operation}.hex")
    with open(output_file_path, "w") as f:
        f.write(hex_data)

    st.success(f"✅ Hex file saved: `{output_file_path}`")

    # Read hex back and reconstruct image
    with open(output_file_path, "r") as f:
        loaded_hex = f.read()

    def hex_to_image(hex_string, size):
        try:
            pixels = [(int(hex_string[i:i+2], 16),
                       int(hex_string[i+2:i+4], 16),
                       int(hex_string[i+4:i+6], 16))
                      for i in range(0, len(hex_string), 6)]
            img = Image.new("RGB", size)
            img.putdata(pixels)
            return img
        except Exception as e:
            st.error("Error reconstructing image from hex.")
            return None

    reconstructed_image = hex_to_image(loaded_hex, processed_image.size)

    if reconstructed_image:
        st.image(reconstructed_image, caption="🖼️ Reconstructed Image from HEX", use_column_width=True)
