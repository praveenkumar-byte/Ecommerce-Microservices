FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.9-slim
WORKDIR /app
RUN useradd -m order-service
COPY --from=builder /root/.local /root/.local
COPY /app/main.py .
ENV PATH=/root/.local/bin:$PATH
USER order-service
CMD ["python","main.py"]