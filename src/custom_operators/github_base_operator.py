import requests
from typing import Union
from airflow.models import Variable
from airflow.utils.log.logging_mixin import LoggingMixin
from airflow.models.baseoperator import BaseOperator
from airflow.providers.http.hooks.http import HttpHook


class GitHubOperator(BaseOperator, LoggingMixin):

    def __init__(self, repo_name: str, end_point: str = "", **kwargs) -> None:
        super().__init__(**kwargs)
        self.repo_name = repo_name
        self.end_point = end_point
        self.github_conn_id = Variable.get("github_conn_id")
        self.owner = Variable.get("owner")
        self.base_url = "/".join((Variable.get("url"), self.owner, self.repo_name))
        self.url = self.set_url()

    def set_url(self) -> str:
        """Sets the URL dynamically based on end_point."""
        return "/".join((self.base_url, self.end_point))

    def get_connection(self) -> requests.Session:
        try:
            self.log.info("Initializing connection to Github API...")
            api_hook = HttpHook(method="GET", http_conn_id=self.github_conn_id)
            conn = api_hook.get_conn()
            self.log.info("Connection ID defined")
            return conn
        except Exception as e:
            self.log.error(e)

    def retrieve_data(self) -> Union[list[dict],dict[str, str]]:
        connection = self.get_connection()
        response = connection.get(self.url)
        data = response.json()
        return data


