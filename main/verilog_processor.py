import os
import cv2
import numpy as np

def image_to_hex_opencv(image_path, hex_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, _ = img_rgb.shape
    with open(hex_path, "w") as f:
        for row in img_rgb:
            for r, g, b in row:
                f.write(f"{r:02x}{g:02x}{b:02x}")
    
    # Save width and height for Verilog testbench
    with open("output/input_width.txt", "w") as wf:
        wf.write(f"{w:x}")
    with open("output/input_height.txt", "w") as hf:
        hf.write(f"{h:x}")

    return (w, h)

def hex_to_image_opencv(hex_path, size, output_path):
    with open(hex_path, "r") as f:
        hex_data = f.read()
    pixels = [
        [int(hex_data[i:i+2], 16),
         int(hex_data[i+2:i+4], 16),
         int(hex_data[i+4:i+6], 16)]
        for i in range(0, len(hex_data), 6)
    ]
    pixels = np.array(pixels, dtype=np.uint8).reshape((size[1], size[0], 3))  # H, W, 3
    img_bgr = cv2.cvtColor(pixels, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, img_bgr)
    return img_bgr

def run_verilog(operation):
    if operation == "brightness":
        os.system("iverilog -o sim verilog/brightness.v verilog/tb_brightness.v && vvp sim")
    elif operation == "contrast":
        os.system("iverilog -o sim verilog/contrast.v verilog/tb_contrast.v && vvp sim")
    elif operation == "grayscale":
        os.system("iverilog -o sim verilog/grayscale.v verilog/tb_grayscale.v && vvp sim")
    elif operation == "negation":
        os.system("iverilog -o sim verilog/negation.v verilog/tb_negation.v && vvp sim")
    elif operation == "flip_horizontal":
        os.system("iverilog -o sim verilog/flip_horizontal.v verilog/tb_flip_horizontal.v && vvp sim")


def process_image_opencv(image_path, operation):
    os.makedirs("output", exist_ok=True)
    size = image_to_hex_opencv(image_path, "output/input.hex")
    run_verilog(operation)
    return hex_to_image_opencv("output/processed.hex", size, "output/final_image.png")
