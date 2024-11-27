FROM python:3.12-slim-bookworm

# Working directory
WORKDIR /app

# Install necessary system dependencies including Chrome and Chromedriver
RUN apt-get update && apt-get install -y \
    gettext \
    vim \
    curl \
    unzip \
    wget \
    chromium \
    chromium-driver \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libgbm1 \
    libxcomposite1 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    fonts-liberation \
    && apt-get clean

# Create and activate virtual environment
RUN python -m venv /root/.venv

# Install pip and Python dependencies
RUN /root/.venv/bin/pip install --upgrade pip

# Copy requirements and install the dependencies
COPY requirements.txt .
RUN /root/.venv/bin/pip install -r requirements.txt

# Set Python path for runtime
ENV PYTHONPATH=/app:$PYTHONPATH

# Setup the virtual environment
ENV VIRTUAL_ENV=/root/.venv \
    PATH="/root/.venv/bin:$PATH"

# Copy the application code (including tests and utils)
COPY . .

# Set Chrome options for headless execution
ENV CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER=/usr/bin/chromedriver

# Default command to run the tests
CMD ["pytest", "tests/test_login.py"]
