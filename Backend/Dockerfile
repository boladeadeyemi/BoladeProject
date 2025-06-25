# syntax=docker/dockerfile:1

FROM python:3.13.5

WORKDIR /app

# Copy only what's needed
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all application code (relative to Dockerfile)
COPY . .

# Run the server
CMD ["python", "server.py"] 