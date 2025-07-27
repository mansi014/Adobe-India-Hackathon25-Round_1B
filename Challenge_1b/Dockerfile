# Dockerfile for Challenge_1b – Adobe Hackathon 2025

FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Copy source code and requirements
COPY process_documents.py /app/
COPY approach_explanation.md /app/

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy collections (optional if you mount them during runtime)
COPY Collection_1/ /app/Collection_1/
COPY Collection_2/ /app/Collection_2/
COPY Collection_3/ /app/Collection_3/

# Default command (can be overridden)
CMD ["python", "process_documents.py"]
