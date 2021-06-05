from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from elasticsearch_plugin.hooks.elastic_hook import ElasticHook
from elasticsearch_plugin.operators.postgres_to_elastic import PgToEsOperator

default_args = {
    'start_date' : datetime(2021, 5, 1)
}

def _print_es_info():
    hook = ElasticHook()
    print(hook.info())

with DAG('elasticsearch_dag', schedule_interval='@daily', 
        catchup = False,
        default_args=default_args) as dag:
    
    print_es_info = PythonOperator(
        task_id = 'print_es_info',
        python_callable = _print_es_info
    )

    connections_to_es = PgToEsOperator(
        task_id = 'connections_to_es',
        sql = 'SELECT * FROM connection;',
        index = 'connections'
    )

print_es_info >> connections_to_es