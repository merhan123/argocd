# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app files
COPY app.py .

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
