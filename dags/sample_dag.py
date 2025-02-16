"""DAG Definition for GitHub Data Retrieval

This module defines an Apache Airflow DAG that orchestrates multiple custom
GitHub-related tasks, including authentication, retrieving pull requests,
commits, issues, and branches from a GitHub repository.

The DAG consists of the following tasks:
- AuthOperator: Authenticates the connection to the GitHub API.
- WIPOperator: Retrieves work-in-progress (draft) pull requests.
- CommitRetrieverOperator: Retrieves commit data from the repository.
- IssueOperator: Retrieves issues from the repository.
- BranchOperator: Retrieves branches from the repository.

The tasks are executed sequentially, starting from authentication and
proceeding through data retrieval tasks.

This DAG is intended to provide an overview of the operation of the custom Airflow operators
"""
import datetime

from airflow import DAG
from src.custom_operators.auth_operator import AuthOperator
from src.custom_operators.wip_operator import WIPOperator
from src.custom_operators.commit_retriever_operator import CommitRetrieverOperator
from src.custom_operators.issue_operator import IssueOperator
from src.custom_operators.branch_operator import BranchOperator


dag = DAG(dag_id='github_dag',
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

t5 = BranchOperator(task_id="brancher",
                    repo_name="python",
                    end_point="branches",
                    dag=dag)

t1 >> t2 >> t3 >> t4 >> t5