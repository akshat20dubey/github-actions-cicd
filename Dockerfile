# Use official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy scripts into the container
COPY scripts/ .

# Install required Python libraries
RUN pip install requests

# Run the server checker script when container starts
CMD ["python", "server-checker.py"]
