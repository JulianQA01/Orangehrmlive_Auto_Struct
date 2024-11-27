# The builder image, used to build the virtual environment and install dependencies
FROM python:3.12-slim-bookworm AS builder

# Install dependencies and Chromium
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    chromium \
    chromium-driver \
    && apt-get clean

# Set environment variables for Chromium
ENV CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER=/usr/bin/chromedriver

# Set PYTHONPATH so that Python can find our app code
ENV PYTHONPATH=/app

# Set working directory
WORKDIR /app

# Copy the code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Final runtime image
FROM python:3.12-slim-bookworm

# Install Chromium and ChromeDriver
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && apt-get clean

# Set environment variables for Chromium
ENV CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER=/usr/bin/chromedriver

# Set PYTHONPATH so that Python can find our app code
ENV PYTHONPATH=/app

# Set working directory
WORKDIR /app

# Copy the code and virtual environment from the builder
COPY --from=builder /app /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run default cmd
CMD ["pytest", "tests/test_login.py"]
