"""CommitRetrieverOperator Module.

This module defines a custom Airflow operator, `CommitRetrieverOperator`, which extends the `GitHubOperator` class.
It is used to retrieve and filter commits from a GitHub repository based on specified criteria such as branch name,
commit author, and commit date.

Classes:
    CommitRetrieverOperator: An Airflow operator to retrieve and filter commits from a GitHub repository.
"""
from .github_base_operator import GitHubOperator


class CommitRetrieverOperator(GitHubOperator):
    """Custom Airflow Operator to retrieve and filter GitHub commits.

    This operator extends `GitHubOperator` and retrieves commits from a GitHub repository. It allows
    filtering based on branch name, commit author, and commit date.

    Attributes:
        branch_name (str): Optional; branch name to filter commits.
        commit_author (str): Optional; author name to filter commits.
        commit_date (str): Optional; date (YYYY-MM-DD) to filter commits.
        endpoint (str): GitHub API endpoint for retrieving commits.
        Inherits other attributes from `GitHubOperator`.
    """
    def __init__(self, branch_name: str = None, commit_author: str = None, commit_date: str = None, **kwargs):
        """Initializes the CommitRetrieverOperator with optional filtering criteria.

        Args:
            branch_name (str, optional): Name of the branch to filter commits.
            commit_author (str, optional): Author name to filter commits.
            commit_date (str, optional): Date (YYYY-MM-DD) to filter commits.
            **kwargs: Additional keyword arguments passed to `GitHubOperator` and `BaseOperator`.
        """
        super().__init__(**kwargs)
        self.branch_name = branch_name
        self.commit_author = commit_author
        self.commit_date = commit_date  # YYYY-MM-DD input format
        self.endpoint = "commits?sha={}".format(self.branch_name) if self.branch_name else "commits"

    def execute(self, context: dict) -> list:
        """Executes the retrieval and filtering of GitHub commits.

        Retrieves commits from the GitHub repository and filters them based on the provided
        branch name, commit author, and commit date.

        Args:
            context (dict): Airflow task execution context.

        Returns:
            list: A list of dictionaries representing filtered GitHub commits.

        Raises:
            Exception: If the retrieval or filtering process encounters an error.
        """
        try:
            commits_data = self.retrieve_data()
            commits = [commit for commit in commits_data
                       if (self.commit_author is None
                           or commit["commit"]["author"]["name"] == self.commit_author)
                       and (self.commit_date is None
                           or commit["commit"]["author"]["date"].split("T")[0] == self.commit_date)]

            if len(commits) == 0:
                self.log.info("There is no commit with these conditions.")
            self.log.info("Number of commits: {}".format(str(len(commits))))
            return commits
        except Exception as e:
            self.log.error("Failed to retrieve commits: {}".format(e))
            raise
