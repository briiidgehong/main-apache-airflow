from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def hello_python_def(task_id):
    print("hello python operator ! " + task_id)


default_args = {
    "owner": "briiidgehong",
    "retries": 3,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="first_dag",
    default_args=default_args,
    description="first_dag_description",
    start_date=datetime(2022, 8, 20, 0),
    schedule_interval="@hourly",
) as dag:
    task1 = BashOperator(task_id="task_1", bash_command="echo hello task_1")
    task2 = BashOperator(task_id="task_2", bash_command="echo hello task_2")
    task3 = BashOperator(task_id="task_3", bash_command="echo hello task_3")
    task4 = PythonOperator(
        task_id="task_4",
        python_callable=hello_python_def,
        op_kwargs={"task_id": "task_4"},
    )
    # task1 >> task2
    # task1 >> task3
    task1 >> [task2, task3] >> task4
