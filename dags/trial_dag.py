import datetime

from airflow import DAG
from airflow.models import Variable
from airflow.providers.http.hooks.http import HttpHook
from airflow.operators.python import PythonOperator

end_point = Variable.get('owner') + "/" + "python"


def get_connection() -> bool:
    try:
        print("Initializing connection to Github API...")
        api_hook = HttpHook(method="GET", http_conn_id="github_conn")
        conn = api_hook.get_conn()
        print("Connection ID is defined")
        return conn
    except Exception as e:
        print(e)
        raise ConnectionError


def check_token():
    try:
        connection = get_connection()
        response = connection.get(Variable.get("url") + "/" + Variable.get('owner') + "/" + "python/pulls")
        data = response.json()
        wip_prs = []
        for pull_request in data:
            if pull_request["draft"]:
                wip_prs.append(pull_request)
        print("Number of WIP PRs: " + str(len(wip_prs)))
        print("List of WIP PRs: " + str(wip_prs))
        return wip_prs
    except Exception as e:
        print("Connection is not authenticated: {}".format(e))


dag = DAG(dag_id='trial_dag',
          start_date=datetime.datetime.now(),
          schedule_interval=None)





