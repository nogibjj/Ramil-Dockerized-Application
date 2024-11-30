# Use the official Python image as a base
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy all files from the current directory into /app
COPY . /app

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the Flask app's port (default 5000)
EXPOSE 2222

# Define the command to run the application
CMD ["python", "main.py"]