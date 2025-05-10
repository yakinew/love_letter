# FROM python:3.14.0a6-alpine3.21
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies from the requirements file
RUN pip install -r requirements.txt

# Copy the source code directory to the working directory
COPY src .

# Optionally, specify the command to run your application
# For example, if your main script is named 'main.py':
CMD ["python", "main.py"]
