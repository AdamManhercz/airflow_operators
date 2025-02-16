"""GitHubOperator Module

This module defines a custom Airflow operator base class, `GitHubOperator`, designed to interact with the GitHub API.
It facilitates making HTTP requests to retrieve data from GitHub repositories,
leveraging Airflow's `HttpHook` for connection management.

Classes:
    GitHubOperator: An Airflow operator for establishing connection and data retrieving from GitHub API.
"""
import requests
from typing import Union
from airflow.models import Variable
from airflow.utils.log.logging_mixin import LoggingMixin
from airflow.models.baseoperator import BaseOperator
from airflow.providers.http.hooks.http import HttpHook


class GitHubOperator(BaseOperator, LoggingMixin):
    """ Custom Airflow Operator to interact with the GitHub API.

        This operator is used to retrieve data from a specified GitHub repository by making HTTP requests
        to the GitHub REST API. It leverages Airflow's HttpHook for connection management.

        Attributes:
            repo_name (str): Name of the GitHub repository to interact with.
            end_point (str): Endpoint path to retrieve specific data from the repository.
            github_conn (str): Airflow connection ID for GitHub API.
            owner (str): GitHub repository owner.
            base_url (str): Base URL constructed using the GitHub API base and repository details.
            url (str): Full API URL constructed dynamically based on the endpoint.
    """

    def __init__(self, repo_name: str, end_point: str, **kwargs) -> None:
        """Initializes the GitHubOperator with repository and endpoint details.

        Args:
            repo_name (str): The name of the GitHub repository.
            end_point (str, optional): Additional API endpoint to append to the base URL. Defaults to "".
            **kwargs: Additional keyword arguments passed to the BaseOperator.
        """
        super().__init__(**kwargs)
        self.repo_name = repo_name
        self.end_point = end_point
        self.github_conn = Variable.get("github_conn")
        self.owner = Variable.get("owner")
        self.base_url = "/".join((Variable.get("base_url"), self.owner, self.repo_name))
        self.url = self.set_url()

    def set_url(self) -> str:
        """ Constructs and returns the full URL for the GitHub API request.

        Returns:
            str: The full API URL including the base URL and the endpoint.
        """
        return "/".join((self.base_url, self.end_point))

    def get_connection(self) -> requests.Session:
        """ Establishes a connection to the GitHub API using Airflow's HttpHook.

        Returns:
            requests.Session: A configured session object for making HTTP requests to the GitHub API.

        Raises:
            Exception: If the connection setup fails, logs the error.
        """
        try:
            self.log.info("Initializing connection to Github API...")
            api_hook = HttpHook(method="GET", http_conn_id=self.github_conn)
            conn = api_hook.get_conn()
            self.log.info("Connection ID defined")
            return conn
        except Exception as e:
            self.log.error(e)

    def retrieve_data(self) -> Union[list[dict], dict[str, str]]:
        """ Makes a GET request to the constructed GitHub API URL and retrieves data.

        Returns:
            Union[list[dict], dict[str, str]]: The API response data parsed as JSON.
        """
        connection = self.get_connection()
        response = connection.get(self.url)
        data = response.json()
        return data


