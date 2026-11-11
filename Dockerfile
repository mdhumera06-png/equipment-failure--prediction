
# Use Python 3.13 as the base image
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Configure Python environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

# Copy requirements file
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Copy API files
COPY api/ ./api/

# Copy trained model
COPY models/ ./models/

# Expose API port
EXPOSE 8000

# Start FastAPI application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
