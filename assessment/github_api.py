import os
from typing import Generator

import requests
from dotenv import load_dotenv

from base_repository import BaseRepository
from github_error import GitHubError
from repository import Repository, RepositoryStats

load_dotenv()


class GitHubAPI:
    BASE_URL = "https://api.github.com"
    HEADERS = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"}

    @classmethod
    def get_repository(cls, full_name: str) -> Repository:
        url = f"{cls.BASE_URL}/repos/{full_name}"
        response = requests.get(url, headers=cls.HEADERS)

        if response.status_code != 200:
            raise GitHubError(f"ошибка {response.status_code}: {response.json().get('message')}")

        data = response.json()

        stats = RepositoryStats(
            stars=data["stargazers_count"],
            watchers=data["watchers_count"],
            forks=data["forks_count"],
            open_issues=data["open_issues_count"]
        )

        return Repository(
            id=data["id"],
            name=data["name"],
            full_name=data["full_name"],
            language=data["language"],
            stats=stats
        )

    @classmethod
    def get_all(cls, owner: str, owner_type: str, get_full: bool = False) -> Generator:
        page = 1

        while True:
            url = f"{cls.BASE_URL}/{owner_type}/{owner}/repos"
            response = requests.get(url, params={"per_page": 100, "page": page}, headers=cls.HEADERS)

            if response.status_code != 200:
                raise GitHubError(f"ошибка {response.status_code}: {response.json().get('message')}")

            repos = response.json()

            if len(repos) == 0:
                break

            for repo in repos:
                if get_full:
                    yield cls.get_repository(repo["full_name"])
                else:
                    yield BaseRepository(name=repo["name"], full_name=repo["full_name"])

            if len(repos) < 100:
                break

            page += 1
