# Use Python base image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy your project files into the container
COPY src/ src/
COPY logs/ logs/
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Run your log parser script
CMD ["python", "src/log_parser.py"]