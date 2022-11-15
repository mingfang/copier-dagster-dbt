FROM python:3.10-slim

RUN apt update
RUN apt install -y git

RUN pip install dagster dagster-postgres dagster-docker dagster_k8s

WORKDIR /opt/dagster

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app /opt/dagster/app
RUN dbt deps --project-dir app/dbt_parent

EXPOSE 4000

CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-f", "app/repository.py"]