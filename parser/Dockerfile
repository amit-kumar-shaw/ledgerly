FROM python:3.13-slim

# system dependencies for PyMuPDF and Pandas dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends libmupdf-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src

EXPOSE 8000

CMD ["fastapi", "run", "src/main.py"]
