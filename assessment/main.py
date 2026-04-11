import itertools

from github_api import GitHubAPI
from github_error import GitHubError


def main():
    try:
        repo = GitHubAPI.get_repository("psf/requests")
        print(repo)
    except GitHubError as e:
        print(e)

    try:
        repos = list(itertools.islice(GitHubAPI.get_all("microsoft", "orgs", get_full=True), 50))

        best = repos[0]
        for repo in repos:
            if repo.stats.stars > best.stats.stars:
                best = repo

        print(f"Репозиторий с наибольшим количеством звезд: {best}")
    except GitHubError as e:
        print(e)


main()
