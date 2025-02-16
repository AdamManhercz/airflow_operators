"""AuthOperator Module

This module defines a custom Airflow operator, `AuthOperator`, which extends the `GitHubOperator` class.
It is specifically used to verify authentication with the GitHub API by checking the validity of the provided
credentials and API access permissions.

The operator sends a HEAD request to the repository URL to confirm that the authentication is valid and the
GitHub API can be accessed without authorization issues.

Classes:
    AuthOperator: An Airflow operator to verify authentication with the GitHub API.
"""
from .github_base_operator import GitHubOperator


class AuthOperator(GitHubOperator):
    """Custom Airflow Operator to authenticate with the GitHub API.

    This operator extends `GitHubOperator` to perform an authentication check by sending a HEAD request
    to the GitHub repository URL. It verifies that the provided credentials allow access to the API.

    Attributes:
        Inherits all attributes from `GitHubOperator`.
    """
    def __init__(self, **kwargs):
        """Initializes the AuthOperator by invoking the parent class constructor.

        Args:
            **kwargs: Additional keyword arguments passed to the `GitHubOperator` and `BaseOperator`.
        """
        super().__init__(**kwargs)

    def execute(self, context: dict) -> None:
        """Executes the authentication check against the GitHub API.

        Sends a HEAD request to the base URL to verify if the authentication credentials are valid.
        Logs an error and raises a `ConnectionError` if authentication fails.

        Args:
            context (dict): Airflow task execution context.

        Raises:
            ConnectionError: If credentials are invalid or access is forbidden.
            Exception: If an unexpected error occurs during the connection attempt.
        """
        try:
            connection = self.get_connection()
            check = connection.head(self.base_url)
            print(self.base_url)
            if check.status_code in [401, 403]:
                raise ConnectionError("Invalid credentials or Access forbidden, possibly rate-limited.")
            self.log.info("Connection is authenticated to Github API")
        except Exception as e:
            self.log.error("Connection is not authenticated: {}".format(e))
            raise
