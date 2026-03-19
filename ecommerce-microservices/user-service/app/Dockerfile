# install dependencies stage
FROM python:3.9 as builder
WORKDIR /app
COPY ../../requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# runtime stage
FROM python:3.9-slim
# create a working directory
WORKDIR /app
# add a non-root user to run the application
RUN useradd -m user-service

COPY --from=builder /root/.local /root/.local
COPY . .

#set the PATH environment variable to include the local bin directory where pip installs packages for the user
ENV PATH=/root/.local/bin:$PATH
#switch to the non-root user
USER user-service

CMD ["python","app.py"]