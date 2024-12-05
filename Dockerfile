# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir ultralytics gradio pillow

# Expose port 7860 for the Gradio app
EXPOSE 7860

# Run the application
CMD ["python", "gradio_yolo_app.py"]
