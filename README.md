# docker-apache-airflow

ref) airflow tutorial / https://www.youtube.com/watch?v=K9AnJ9_ZAXE&t=1642s / https://github.com/apache/airflow

### - 1. RUN AIRFLOW IN PYTHON ENV 
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

### - 2. RUN AIRFLOW IN DOCKER
### - 3. RUN AIRFLOW IN DOCKER
AIRFLOW CORE CONCEPTS
AIRFLOW TASK LIFECYCLE
AIRFLOW BASIC ARCHITECTURE
10:44 - Run Airflow in Docker
17:55 - Airflow Basics and Core Concepts
21:55 - Airflow Task Lifecycle
26:19 - Airflow Basic Architecture
28:14 - Airflow DAG with Bash Operator
40:09 - Airflow DAG with Python Operator
45:04 - Data Sharing via Airflow XComs
52:53 - Airflow Task Flow API
57:56 - Airflow Catch Up and Backfill
01:02:09 - Airflow Scheduler with Cron Expression
01:07:25 - Airflow Connection to Postgres
01:08:58 - Airflow Postgres Operator
01:19:30 - Airflow Docker Install Python Package 2 ways
01:29:34 - Airflow AWS S3 Sensor Operator
01:42:37 - Airflow Hooks S3 PostgreSQL




