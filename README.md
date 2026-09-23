# Student Task Manager API

A simple containerized REST API built with Flask and Docker, designed for a cloud/distributed systems assessment.

## Endpoints

- GET `/health`
- GET `/tasks`
- POST `/tasks`
- DELETE `/tasks/<id>`

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000/health

## Run tests

```bash
pytest -q
```

## Run with Docker

```bash
docker build -t student-task-api .
docker run -p 5000:5000 student-task-api
```

Then open http://localhost:5000/health

## Cloud architecture

User → AWS EC2 → Docker Container → Flask API

Docker image is intended to be stored in Amazon ECR and pulled by the EC2 instance.
