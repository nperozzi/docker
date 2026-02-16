# Fetch ubuntu image
FROM python:3.11-slim

# Set working directory
WORKDIR /src

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./src .

# Expose port
EXPOSE 5000


# Command to be invoked when the container gets started
ENTRYPOINT ["python", "flask-test.py"]
