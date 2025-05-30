# Base image for Python backend
FROM python:3.10-slim AS backend

# Set working directory
WORKDIR /app

# Install backend dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ /app/backend
COPY uploads/ /app/uploads
COPY processed/ /app/processed

# ---- Frontend Build Phase ----
FROM node:18-alpine AS frontend

# Set working directory
WORKDIR /app/frontend

# Copy frontend code
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

# ---- Final Combined Image ----
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy backend layer
COPY --from=backend /app /app

# Copy frontend build into backend static folder (if serving via backend)
COPY --from=frontend /app/frontend/build /app/frontend/build

# Install any additional system dependencies if needed (optional)
RUN apt-get update && apt-get install -y curl

# Expose backend port
EXPOSE 8000

# Start the backend app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
