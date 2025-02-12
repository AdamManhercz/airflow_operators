from custom_operators.github_base_operator import GitHubOperator


class WIPOperator(GitHubOperator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, context: dict) -> list:
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
