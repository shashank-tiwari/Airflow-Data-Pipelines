from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


default_args = {
    'start_date' : datetime(2021, 5, 1)
}

with DAG('parallel_dag', schedule_interval='@daily', 
        catchup = False,
        default_args=default_args) as dag:

    task1 = BashOperator(
        task_id = 'task1',
        bash_command = 'sleep 3'
    )

    task2 = BashOperator(
        task_id = 'task2',
        bash_command = 'sleep 3'
    )

    task3 = BashOperator(
        task_id = 'task3',
        bash_command = 'sleep 3'
    )

    task4 = BashOperator(
        task_id = 'task4',
        bash_command = 'sleep 3'
    )

    task1 >> [task2, task3] >> task4
    
