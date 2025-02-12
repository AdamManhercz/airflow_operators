import datetime

from airflow import DAG
from src.custom_operators import AuthOperator
from src.custom_operators import WIPOperator
from src.custom_operators import CommitRetrieverOperator
from src.custom_operators import IssueOperator
from src.custom_operators.branch_operator import BranchOperator

default_task_args = {
    "owner": "airflow",

}

dag = DAG(dag_id='test_dag',
          start_date=datetime.datetime.now(),
          schedule_interval=None)


t1 = AuthOperator(task_id='auth_connection',
                  repo_name="python",
                  dag=dag)

t2 = WIPOperator(task_id="wip_pull_requests",
                 repo_name="python",
                 end_point="pulls",
                 dag=dag)

t3 = CommitRetrieverOperator(task_id="commit_retriever",
                             repo_name="python",
                             end_point="commits",
                             dag=dag)

t4 = IssueOperator(task_id="issue_retriever",
                   repo_name="python",
                   end_point="issues",
                   dag=dag)
t5 = IssueOperator(task_id="issue_retriever",
                   repo_name="python",
                   end_point="issues",
                   dag=dag)

t1 >> t2 >> t3 >> t4
