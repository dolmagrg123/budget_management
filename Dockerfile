#  Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port the app runs on (change if your app uses a different port)
EXPOSE 5000

# Run the Python application when the container starts
CMD ["python", "main.py"]