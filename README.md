# docker-apache-airflow
docker-apache-airflow
방식1. fast-setup
ref)[ https://austcoconut.tistory.com/entry/%EB%AC%B4%EC%9E%91%EC%A0%95-%EB%94%B0%EB%9D%BC%ED%95%98%EA%B8%B0-LinuxUbuntu-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-Airflow-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0 ](https://jybaek.tistory.com/922)

```
$ curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.1.0/docker-compose.yaml'

$ mkdir ./dags ./logs ./plugins
$ echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

$ docker-compose up airflow-init
$ docker-compose up -d
```

방식2. production 환경 구축
