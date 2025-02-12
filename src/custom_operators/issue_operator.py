from custom_operators.github_base_operator import GitHubOperator


class IssueOperator(GitHubOperator):

    def __init__(self, assignee: str = None, milestone: str = None, **kwargs):
        super().__init__(**kwargs)
        self.assignee = assignee
        self.milestone = milestone

    def execute(self, context: dict) -> list:
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
            print("Connection is not authenticated: {}".format(e))
