# Use lightweight Python image
FROM python:3.11 AS build

#dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    libgl1 \
    libglib2.0-0 \
    libxcb1 \
    libxext6 \
    libxrender1 \
    libsm6 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

#Create Backend directory
RUN mkdir Backend

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend code
COPY . /app/Backend/

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI
CMD ["python", "-m", "uvicorn", "Backend.Infrastructure.main:app", "--host", "0.0.0.0", "--port", "8000"]