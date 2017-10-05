import os

from github import Github


class DataFetcher:
    """TODO" docstring"""
    def __init__(self):
        # TODO: check for non-existing settings
        access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
        self.repository_name = os.environ.get('GITHUB_REPOSITORY_NAME')

        self.github = Github(login_or_token=access_token)

    def get_pull_requests(self):
        """TODO" docstring"""
        repo = self.github.get_repo('reciprocity/zengrc')
        pull_requests = repo.get_pulls(state='all')

        i = 0
        result = []
        while True:
            data_page = pull_requests.get_page(i)
            if not data_page:
                break
            result.extend(data_page)
            i += 1
            if i > 2:  # TODO: later remove
                break

        return result
