FROM apache/airflow:2.10.3-python3.12

# Set Airflow home and other environment variables
ENV AIRFLOW_HOME=/opt/airflow
ENV PYTHONPATH="/opt/airflow/src:$PYTHONPATH"
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
ENV AIRFLOW__CORE__EXECUTOR=SequentialExecutor

USER root

# Install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

USER airflow

# Install Python dependencies
COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

# Set up plugins directory
COPY ./src/custom_operators /opt/airflow/src/custom_operators

# Initialize the Airflow database and create a user
RUN airflow db init
RUN airflow users create \
    --username airflow \
    --firstname Firstname \
    --lastname Lastname \
    --email admin@example.com \
    --role Admin \
    --password airflow

# Run Airflow services
CMD ["bash", "-c", "airflow scheduler & airflow webserver -p 8080"]
