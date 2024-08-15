# 1. Use the official Python base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file and install any required Python packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the Python script into the container
COPY your_script.py .

