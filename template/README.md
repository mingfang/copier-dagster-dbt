# {{ project_name }}

## Requirements
- [dbt](https://github.com/dbt-labs/dbt-core)
- [dagster](https://github.com/dagster-io/dagster)

## Installation
```shell
pip install -r requirements.txt
```

## Local Dev

### Run `dagit`
```shell
./dagit.sh
```

### Run `dagster-daemon`
```shell
./dagster-daemon.sh
```

### Run in Docker
```shell
./docker-run.sh
```

### Deployment
[Deploy to Kubernetes using Terraform](https://github.com/mingfang/terraform-k8s-modules/tree/master/examples/dagster)
