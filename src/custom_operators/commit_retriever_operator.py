from custom_operators.github_base_operator import GitHubOperator


class CommitRetrieverOperator(GitHubOperator):

    def __init__(self, branch_name: str = None, commit_author: str = None, commit_date: str = None, **kwargs):
        super().__init__(**kwargs)
        self.branch_name = branch_name
        self.commit_author = commit_author
        self.commit_date = commit_date  # YYYY-MM-DD input format
        self.endpoint = "commits?sha={}".format(self.branch_name) if self.branch_name else "commits"

    def execute(self, context: dict) -> list:
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
