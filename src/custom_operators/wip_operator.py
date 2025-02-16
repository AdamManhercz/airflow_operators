"""WIPOperator Module

This module defines a custom Airflow operator, `WIPOperator`, which extends the `GitHubOperator` class.
It is used to retrieve pull requests from a GitHub repository
and filter them to identify Work In Progress (WIP) pull requests,
commonly represented by draft pull requests.

Classes:
    WIPOperator: An Airflow operator to retrieve and filter draft pull requests from a GitHub repository.
"""
from .github_base_operator import GitHubOperator


class WIPOperator(GitHubOperator):
    """Custom Airflow Operator to retrieve draft pull requests from GitHub.

    This operator extends `GitHubOperator` and retrieves pull requests from a GitHub repository.
    It filters the pull requests to identify Work In Progress (WIP) PRs, which are marked as drafts.

    Inherits attributes from `GitHubOperator`.
    """
    def __init__(self, **kwargs):
        """Initializes the WIPOperator.

         Args:
             **kwargs: Additional keyword arguments passed to `GitHubOperator` and `BaseOperator`.
         """
        super().__init__(**kwargs)

    def execute(self, context: dict) -> list:
        """Executes the retrieval and filtering of draft pull requests from GitHub.
           Retrieves pull requests from the GitHub repository and filters them to return those marked as drafts (WIP).

           Args:
               context (dict): Airflow task execution context.

           Returns:
               list: A list of dictionaries representing pull requests from the repository. Draft PRs are logged separately.

           Raises:
               Exception: If the retrieval process encounters an error.
           """
        try:
            pull_data = self.retrieve_data()
            wip_prs = [pr for pr in pull_data if pr["draft"]]
            
            if len(wip_prs) == 0:
                self.log.info("There is no PR in Draft status.")
            self.log.info("Number of WIP PRs: {}".format(str(len(wip_prs))))
            return pull_data
        except Exception as e:
            self.log.error("Failed to retrieve WIP PRs: {}".format(e))
            raise
