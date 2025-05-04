# Base Python Image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy project
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Start server (using eventlet because Flask-SocketIO recommends it)
CMD ["python", "run.py"]
