# Airflow Project

## Project Overview

This repository is a fully containerized Apache Airflow project designed to automate workflows involving GitHub operations. 
It leverages custom Airflow operators to interact with GitHub, retrieve issues, commits, and manage pull requests. 
The environment is built using Docker and orchestrated via Docker Compose.

## Repository Structure

my_airflow_project/
│── dags/                      # Sample DAG files
│── logs/                      # Airflow logs
│── src/                       # Custom Airflow operators as a Python package
│   ├── custom_operators/     # Package name
│   │   ├── __init__.py        # Plugin initialization
│   │   ├── github_base_operator.py     # Base operator
│   │   ├── auth_operator.py       # Operator for authentication
│   │   ├── branch_operator.py         # Operator to manage branches
│   │   ├── wip_operator.py         # Operator for work-in-progress tasks
│   │   ├── commit_retriever_operator.py         # Operator to retrieve commits
│   │   ├── issue_operator.py         # Operator to retrieve GitHub issues
│── requirements.txt           # Python dependencies
│── setup.py                   # Packaging configuration
│── secrets.json             # Airflow connection secrets (e.g., GitHub tokens)
│── variables.json             # Airflow variables configuration
│── docker-compose.yaml        # Docker Compose configuration
│── Dockerfile                 # Custom Docker image definition
│── README.md                  # Project documentation

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

