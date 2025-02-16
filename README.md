# Airflow Project

## Project Overview

This repository is a fully containerized Apache Airflow project designed to automate workflows involving GitHub operations. 
It leverages custom Airflow operators to interact with GitHub, retrieve issues, commits, and manage pull requests. 
The environment is built using Docker and orchestrated via Docker Compose.

## Repository Structure

### 1. `dags/`
Contains sample DAG files that define workflows using Airflow.

### 2. `logs/`
Directory for Airflow logs generated during DAG execution.

### 3. `src/custom_operators/`
A Python package for custom Airflow operators. Notable files:
- `github_base_operator.py`: Base class for GitHub-related operators.
- `auth_operator.py`: Handles authentication with GitHub API.
- `branch_operator.py`: Manages GitHub branches.
- `wip_operator.py`: Tracks work-in-progress tasks.
- `commit_retriever_operator.py`: Retrieves commit data from GitHub.
- `issue_operator.py`: Retrieves issue data from GitHub.

### 4. `requirements.txt`
Lists Python dependencies for the project.

### 5. `setup.py`
Defines the packaging configuration for custom operators as a Python package.

### 6. `secrets.json`
Contains secrets such as GitHub API tokens and Airflow connection settings.

### 7. `variables.json`
Holds Airflow variable configurations, e.g., repository names.

### 8. `docker-compose.yaml`
Configuration file for setting up Airflow, PostgreSQL, and Redis services via Docker Compose.

### 9. `Dockerfile`
Specifies custom Docker image for the project.



## Key Features

Custom Airflow Operators: Customized operators to interact with the GitHub API (e.g., retrieve issues, commits, manage branches).

Docker & Docker Compose: Fully containerized environment for easy setup and deployment.

Secrets Management: Configured through secrets.json for secure connection storage.

Package Structure: Custom operators organized as a Python package for modularity and scalability.

## Setup Instructions

### 1. Clone this repository

git clone <repository_url>
cd my_airflow_project

### 2. Build and Start Airflow

docker-compose up --build

### 3. Access Airflow UI

Open your browser and visit http://localhost:8080

#### Username&Password: airflow

### Configuration

Secrets: Place your API tokens and connection secrets in secrets.json.

Airflow Variables: Define runtime variables in variables.json.

Python Dependencies: List all dependencies in requirements.txt.

