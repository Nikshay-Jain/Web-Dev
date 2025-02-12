# Use the official Python image from the Docker Hub
FROM python:3.8.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy all the application code into the container
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "main.py"]