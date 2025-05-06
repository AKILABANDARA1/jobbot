FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user with fixed UID/GID
RUN groupadd -g 10001 appuser && \
    useradd -u 10001 -g appuser -s /bin/sh -m appuser && \
    chown -R 10001:10001 /app

# Switch to the non-root user
USER 10001

# Start the app using uvicorn
CMD ["uvicorn", "app.__init__:app", "--host", "0.0.0.0", "--port", "8000"]
