import streamlit as st
import cv2
import numpy as np
from verilog_processor import process_image_opencv

st.title("🧠 Brightness Enhancement using Verilog + OpenCV 🧊")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file:
    # Save input image temporarily
    temp_path = "output/temp_input_image.png"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    # Display original image
    img = cv2.imread(temp_path)
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Original Image", use_column_width=True)

    if st.button("✨ Apply Brightness (Verilog)"):
        processed_img = process_image_opencv(temp_path)
        st.image(cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB), caption="Processed Image (From Verilog)", use_column_width=True)
