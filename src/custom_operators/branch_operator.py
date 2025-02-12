from custom_operators.github_base_operator import GitHubOperator


class BranchOperator(GitHubOperator):

    def __init__(self):
        super().__init__()
        self.endpoint = "branches"

    def execute(self, context: dict) -> list:
        try:
            branches_data = self.retrieve_data()
            branch_names = [branch["name"] for branch in branches_data]

            if len(branches_data) == 0:
                self.log.info("There is no available branch for this repository.")
            self.log.info("Number of branches: {}".format(str(len(branch_names))))
            self.log.info("Available branches: {}".format(branch_names))
            return branches_data
        except Exception as e:
            print("Connection is not authenticated: {}".format(e))
