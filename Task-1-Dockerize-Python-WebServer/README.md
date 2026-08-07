# Dockerized Python Web Server

A simple Python Flask web server containerized with Docker.

## Features

- Python Flask web application
- Dockerized using a custom Dockerfile
- Runs as a non-root user
- Exposes port 5000
- Returns "Hello World" on the root endpoint

---

## Project Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
└── .dockerignore
```

---

## Build the Docker Image

```bash
docker build -t flask-hello .
```

---

## Run the Container

```bash
docker run -d \
  --name flask-app \
  -p 5000:5000 \
  flask-hello
```

---

## Test

Using curl:

```bash
curl http://localhost:5000
```

Expected output:

```
Hello World
```

Or open in your browser:

```
http://<EC2_PUBLIC_IP>:5000
```

---

## Verify the Container Runs as a Non-Root User

```bash
docker exec -it flask-app whoami
```

Expected output:

```
appuser
```

---

## Stop the Container

```bash
docker stop flask-app
```

---

## Remove the Container

```bash
docker rm flask-app
```

---

## Recreate the Container

```bash
docker run -d \
  --name flask-app \
  -p 5000:5000 \
  flask-hello
```

The application works without any additional setup because everything it needs is already packaged inside the Docker image.

---

## Technologies Used

- Python 3.12
- Flask
- Docker
