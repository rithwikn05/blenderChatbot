# Use a base image
FROM python:3.9-slim

# Install necessary dependencies for Blender
RUN apt-get update && apt-get install -y wget xz-utils

# Download Blender 4.0
RUN wget https://download.blender.org/release/Blender4.0/blender-4.0.0-linux-x64.tar.xz && \
    tar -xf blender-4.0.0-linux-x64.tar.xz && \
    rm blender-4.0.0-linux-x64.tar.xz

# Set Blender executable in $PATH
ENV PATH="/blender-4.0.0-linux-x64:${PATH}"

# Set up your application files and dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code into the container
COPY . .

# Expose the necessary port for your Flask application
EXPOSE 5000

# Command to run your Flask application
CMD ["python", "app.py"]
