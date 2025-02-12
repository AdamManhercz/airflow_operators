from custom_operators.github_base_operator import GitHubOperator


class AuthOperator(GitHubOperator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, context: dict) -> None:
        try:
            connection = self.get_connection()
            check = connection.head(self.base_url)
            if check.status_code in [401, 403]:
                raise ConnectionError("Invalid credentials or Access forbidden, possibly rate-limited.")
            self.log.info("Connection is authenticated to Github API")
        except Exception as e:
            self.log.error("Connection is not authenticated: {}".format(e))
