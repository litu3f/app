FROM runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04

WORKDIR /app

COPY backend/ /app/backend
COPY requirements.txt .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [""]  # clears NVIDIA’s default entrypoint

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
