from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy import DummyOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
        'dummy_dag',
         start_date=datetime(2022, 6, 20),
         schedule_interval='@hourly',
         default_args=default_args,
         template_searchpath='/Users/imachado/Documentos/Desarrollo/Alkemy/OT234-python/include',
         catchup=False
         ) as dag:
         
        dummyTask = DummyOperator(
        task_id="dummyTask",
        postgres_conn_id="alkemy",
        sql="UAIn_2020-09-01_2021-02-01_OT234-16.sql"
        )

        dummyTask
