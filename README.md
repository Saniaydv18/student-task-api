# Student Task Manager API

A simple containerized REST API built with Flask and Docker, deployed as a cloud web service for a distributed systems/cloud technology assessment.

## Project Overview

The Student Task Manager API allows users to view, create, and delete tasks through REST API endpoints.

The project demonstrates:

- REST API development using Flask
- Docker containerization
- Cloud deployment using Render
- Automated testing using pytest
- CI/CD using GitHub Actions
- GitHub branch protection using required CI checks

## Technologies Used

- Python
- Flask
- Docker
- pytest
- GitHub
- GitHub Actions
- Render

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Checks whether the API is running |
| GET | `/tasks` | Returns all tasks |
| POST | `/tasks` | Creates a new task |
| DELETE | `/tasks/<id>` | Deletes a task |

## Example

### Health Check

```http
GET /health

## Cloud Deployment

The application is deployed using Render as a Docker-based cloud web service.

### Live API

https://student-task-api-29ed.onrender.com

### Health Check

https://student-task-api-29ed.onrender.com/health

## System Architecture

```text
                 User / Browser
                       |
                       v
                Internet Request
                       |
                       v
              +------------------+
              |      Render      |
              |  Cloud Service   |
              +------------------+
                       |
                       v
              +------------------+
              | Docker Container |
              |                  |
              |   Flask API      |
              +------------------+
                       |
                       v
                 REST Endpoints
             /health /tasks etc.

## CI/CD Pipeline

```text
Developer pushes code
        |
        v
   GitHub Repository
        |
        v
   GitHub Actions
        |
        v
   Run 5 automated tests
        |
    +---+---+
    |       |
   FAIL    PASS
    |       |
    v       v
   STOP   Render
           Deployment
              |
              v
        Live Application