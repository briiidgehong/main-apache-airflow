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
docker-compose --version *(> v1.29.1)

# download docker-compose.yaml
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.3/docker-compose.yaml'

- airflow-scheduler- 스케줄러 는 모든 작업과 DAG를 모니터링한 다음 종속성이 완료되면 작업 인스턴스를 트리거합니다
- airflow-webserver- 웹서버는 에서 사용할 수 있습니다 http://localhost:8080
- airflow-worker- 스케줄러에 의해 주어진 작업을 실행하는 작업자
- airflow-init- 초기화 서비스
- postgres- 데이터베이스
- redis- redis - 스케줄러에서 작업자에게 메시지를 전달하는 브로커


# Initializing Environment
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
.env file -> AIRFLOW_UID=50000

# Initialize the database
docker-compose up airflow-init

# Running Airflow
docker-compose up
0.0.0.0:8080 (id: airflow / pass: airflow)

# cleaning
docker-compose down --volumes --rmi all

```
### - Airflow Basics and Core Concepts
### - Airflow Task Lifecycle
<img width="870" alt="스크린샷 2022-08-19 오후 8 08 04" src="https://user-images.githubusercontent.com/73451727/185606684-698ceb33-5471-477a-8577-3b598be52e33.png">

### - Airflow Basic Architecture
<img width="883" alt="스크린샷 2022-08-19 오후 8 12 46" src="https://user-images.githubusercontent.com/73451727/185606653-bb0f740d-8046-4fe0-b62c-2df4a0d79d1f.png">

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


ref) 
https://www.youtube.com/watch?v=K9AnJ9_ZAXE&t=1642s
https://airflow.apache.org/docs



