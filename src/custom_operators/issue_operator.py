"""IssueOperator Module

This module defines a custom Airflow operator, `IssueOperator`, which extends the `GitHubOperator` class.
It is used to retrieve and filter issues from a GitHub repository based on specified criteria such as
assignee, milestone, and label.

Classes:
    IssueOperator: An Airflow operator to retrieve and filter issues from a GitHub repository.
"""

from .github_base_operator import GitHubOperator


class IssueOperator(GitHubOperator):
    """Custom Airflow Operator to retrieve and filter GitHub issues.

    This operator extends `GitHubOperator` and retrieves issues from a GitHub repository. It allows
    filtering based on assignee, milestone, and label.

    Attributes:
        assignee (str): Optional; GitHub username to filter issues by assignee.
        milestone (str): Optional; Milestone title to filter issues by milestone.
        Inherits other attributes from `GitHubOperator`.
    """
    def __init__(self, assignee: str = None, milestone: str = None, **kwargs):
        """Initializes the IssueOperator with optional filtering criteria.

           Args:
               assignee (str, optional): GitHub username to filter issues by assignee.
               milestone (str, optional): Milestone title to filter issues by milestone.
               **kwargs: Additional keyword arguments passed to `GitHubOperator` and `BaseOperator`.
        """
        super().__init__(**kwargs)
        self.assignee = assignee
        self.milestone = milestone

    def execute(self, context: dict) -> list:
        """Executes the retrieval and filtering of GitHub issues.

         Retrieves issues from the GitHub repository and filters them based on the provided
         assignee, milestone, and label attributes. Logs the number of matching issues.

         Args:
             context (dict): Airflow task execution context.

         Returns:
             list: A list of dictionaries representing filtered GitHub issues.

         Raises:
             Exception: If the retrieval or filtering process encounters an error.
         """
        try:
            issues_data = self.retrieve_data()
            issues = [issue for issue in issues_data
                      if (self.label is None or self.label in issue["labels"])
                      and (self.assignee is None
                           or issue["assignee"] == self.assignee
                           or self.assignee in issue["assignees"])
                      and (self.milestone is None or issue["milestone"] == self.milestone)]

            if len(issues) == 0:
                self.log.info("There is no issue with these conditions.")
            self.log.info("Number of issues: {}".format(str(len(issues))))
            return issues
        except Exception as e:
            self.log.error("Failed to retrieve issues: {}".format(e))
            raise
