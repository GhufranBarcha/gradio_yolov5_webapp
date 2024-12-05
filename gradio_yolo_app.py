import gradio as gr
from ultralytics import YOLO
from PIL import Image

# Load a pre-trained YOLOv5 model
model = YOLO("yolov5n.pt")

def detect_objects(image):
    """
    Perform object detection on the uploaded image.
    """
    # Run YOLO inference
    results = model(image)
    
    # Annotate the image with predictions
    annotated_image = results[0].plot()
    
    # Return the annotated image
    return Image.fromarray(annotated_image)

# Define the Gradio interface
title = "YOLOv5 Object Detection Model"
description = """Upload an image to detect objects using a pre-trained YOLOv5 model.<br><br>
Deployed by <a href="https://github.com/GhufranBarcha/gradio_yolov5_webapp" target="_blank">Ghufran Barcha</a>."""

# Gradio Interface
interface = gr.Interface(
    fn=detect_objects,
    inputs=gr.Image(type="pil", label="Upload Image"),
    outputs=gr.Image(type="pil", label="Detected Objects"),
    title=title,
    description=description,
    live=True,
)

# Launch the app
interface.launch()
