FROM python:3.9-slim as builder
WORKDIR /app
COPY ../../requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# runtime stage
FROM python:3.9-slim
WORKDIR /app
RUN useradd -m product-service
COPY --from=builder /root/.local /root/.local
COPY main.py .
ENV PATH=/root/.local/bin:$PATH
USER product-service

CMD ["python","main.py"]