# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir gradio==5.8.0 ultralytics==8.3.40 pillow

# Expose port 7860 for the Gradio app
EXPOSE 7860

# Run the application
CMD ["python", "gradio_yolo_app.py"]
