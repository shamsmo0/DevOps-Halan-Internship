# Task 2 - Dockerize Python Web Server with PostgreSQL

## Overview

A Flask web application running inside Docker that retrieves a user's name dynamically from a PostgreSQL database.

The Flask application and PostgreSQL communicate through a user-defined Docker network.

PostgreSQL data is persisted using a Docker named volume.

## Architecture

Browser
   |
   v
Flask Container
   |
   | app-network
   v
PostgreSQL Container
   |
   v
postgres-data Volume

## Technologies

- Python
- Flask
- PostgreSQL
- Docker
- Docker Network
- Docker Volume

## Project Structure

```text
.
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
└── .dockerignore
