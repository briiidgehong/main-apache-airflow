# docker-apache-airflow

ref) airflow tutorial / https://www.youtube.com/watch?v=K9AnJ9_ZAXE&t=1642s / https://github.com/apache/airflow

### - Run Airflow in Python Env
```
python3 -m venv .venv

source .venv/bin/activate

pip install 'apache-airflow==2.3.3' \                                          
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.3/constraints-3.9.txt"
 
export AIRFOWL_HOME=~/totoro/apache-airflow/apache-airflow/tutorial

airflow db init -> airflow.cfg / airflow.db / webserver_config.py / logs

airflow users create \                            
          --username admin \
          --firstname admin \     
          --lastname admin \    
          --role Admin \
          --email admin@example.org

airflow webserver -D -p 8080

0.0.0.0:8080

The scheduler does not appear to be running.
The DAGs list may not update, and new tasks will not be scheduled.

airflow scheduler -D
```

### - Run Airflow in Docker
ref) https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html
```
# dependency
docker --version
docker-compose --version

# download docker-compose.yaml
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.3/docker-compose.yaml'

# Initializing Environment
mkdir -p ./dags ./logs ./plugins
(only linux enviroment not mac os) echo -e "AIRFLOW_UID=$(id -u)" > .env
docker-compose up airflow-init



```
### - Airflow Basics and Core Concepts
### - Airflow Task Lifecycle
### - Airflow Basic Architecture
### - Airflow DAG with Bash Operator
### - Airflow DAG with Python Operator
### - Data Sharing via Airflow XComs
### - Airflow Task Flow API
### - Airflow Catch Up and Backfill
### - Airflow Scheduler with Cron Expression
### - Airflow Connection to Postgres
### - Airflow Postgres Operator
### - Airflow Docker Install Python Package 2 ways
### - Airflow AWS S3 Sensor Operator
### - Airflow Hooks S3 PostgreSQL




