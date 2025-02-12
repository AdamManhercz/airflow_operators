from airflow.plugins_manager import AirflowPlugin
from src.custom_operators.github_base_operator import GitHubOperator
from src.custom_operators.auth_operator import AuthOperator
from src.custom_operators.wip_operator import WIPOperator
from src.custom_operators.commit_retriever_operator import CommitRetrieverOperator
from src.custom_operators.issue_operator import IssueOperator
from src.custom_operators.branch_operator import BranchOperator


class GitHubPlugin(AirflowPlugin):
    name = "github_plugin"
    operators = [GitHubOperator,
                 AuthOperator,
                 WIPOperator,
                 CommitRetrieverOperator,
                 IssueOperator,
                 BranchOperator]
