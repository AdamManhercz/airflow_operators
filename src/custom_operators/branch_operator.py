"""BranchOperator Module

This module defines a custom Airflow operator, `BranchOperator`, which extends the `GitHubOperator` class.
It is used to retrieve a list of branches from a GitHub repository.

Classes:
    BranchOperator: An Airflow operator to retrieve branch names from a GitHub repository.
"""
from .github_base_operator import GitHubOperator


class BranchOperator(GitHubOperator):
    """Custom Airflow Operator to retrieve branches from GitHub.

    This operator extends `GitHubOperator` and retrieves the list of branches from a GitHub repository.

    Inherits attributes from `GitHubOperator`.
    """
    def __init__(self, **kwargs):
        """Initializes the BranchOperator.

          Args:
              **kwargs: Additional keyword arguments passed to `GitHubOperator` and `BaseOperator`.
          """
        super().__init__(**kwargs)

    def execute(self, context: dict) -> list:
        """Executes the retrieval of branches from a GitHub repository.
        Retrieves branch data from the GitHub repository and extracts branch names.

        Args:
            context (dict): Airflow task execution context.

        Returns:
            list: A list of dictionaries representing branch data from the repository.

        Raises:
            Exception: If the retrieval process encounters an error.
        """
        try:
            branches_data = self.retrieve_data()
            branch_names = [branch["name"] for branch in branches_data]

            if len(branches_data) == 0:
                self.log.info("There is no available branch for this repository.")
            self.log.info("Number of branches: {}".format(str(len(branch_names))))
            self.log.info("Available branches: {}".format(branch_names))
            return branches_data
        except Exception as e:
            self.log.error("Failed to retrieve branches: {}".format(e))
            raise
