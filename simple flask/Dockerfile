# Use Python base image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

# Install Flask
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80
EXPOSE 80

# Start Flask app
CMD ["python", "/app/app.py"]
