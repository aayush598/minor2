import streamlit as st
import cv2
import numpy as np
from verilog_processor import process_image_opencv

st.title("🧠 Image Processing using Verilog + OpenCV 🧊")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file:
    temp_path = "output/temp_input_image.png"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    img = cv2.imread(temp_path)
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Original Image", use_column_width=True)

    operation = st.selectbox("Choose an Operation", ["Brightness", "Contrast", "Grayscale", "Negation"])

    if st.button("⚙️ Run Verilog Processing"):
        op_key = operation.lower()
        processed_img = process_image_opencv(temp_path, op_key)
        st.image(cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB), caption=f"Processed Image ({operation})", use_column_width=True)
