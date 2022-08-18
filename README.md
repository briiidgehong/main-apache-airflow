# docker-apache-airflow
https://github.com/apache/airflow

```
docker-apache-airflow
방식1. fast-setup
ref)[https://austcoconut.tistory.com/entry/%EB%AC%B4%EC%9E%91%EC%A0%95-%EB%94%B0%EB%9D%BC%ED%95%98%EA%B8%B0-LinuxUbuntu-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-Airflow-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0](https://jybaek.tistory.com/922)
error) https://github.com/puckel/docker-airflow/issues/631
  - local docker 의 경우, 사용하는 resource를 강제하고 있기때문에 어느정도 리소스를 허용해주어야 돌릴수 있음.


$ curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.1.0/docker-compose.yaml'

$ mkdir ./dags ./logs ./plugins
$ echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

$ docker-compose up airflow-init
$ docker-compose up -d

weserver 접속
  - http://localhost:8080 - airflow/airflow
  
방식2. production 환경 구축
ref) https://airflow.apache.org/docs/docker-stack/build.html
  
 
ref) airflow tutorial
https://www.youtube.com/watch?v=K9AnJ9_ZAXE&t=1642s

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






