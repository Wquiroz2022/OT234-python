from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.postgres_operator import PostgresOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


with DAG('alkemy_conn',
         start_date=datetime(2022, 6, 18),
         max_active_runs=3,
         schedule_interval='@daily',
         default_args=default_args,
         template_searchpath='/Users/imachado/Documentos/Desarrollo/Alkemy/OT234-python/include',
         catchup=False
         ) as dag:

    get_all_pets = PostgresOperator(
    task_id="get_all_pets",
    postgres_conn_id="alkemy",
    sql="UAIn_2020-09-01_2021-02-01_OT234-16.sql"
    )

    get_all_pets