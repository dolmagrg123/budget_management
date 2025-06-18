# Use a base Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY /requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code
COPY / /app

# Create the data directory
RUN mkdir /app/data

# Expose the port the app runs on (change if your app uses a different port)
EXPOSE 5000

# Run the Python application when the container starts
CMD ["python", "main.py"]