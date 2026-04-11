from base_repository import BaseRepository


class RepositoryStats:
    def __init__(self, stars: int, watchers: int, forks: int, open_issues: int):
        self._stars = stars
        self._watchers = watchers
        self._forks = forks
        self._open_issues = open_issues

    @property
    def stars(self) -> int:
        return self._stars

    @property
    def watchers(self) -> int:
        return self._watchers

    @property
    def forks(self) -> int:
        return self._forks

    @property
    def open_issues(self) -> int:
        return self._open_issues

    def __str__(self) -> str:
        return f"stars={self._stars}, watchers={self._watchers}, forks={self._forks}, open_issues={self._open_issues}"


class Repository(BaseRepository):
    def __init__(self, id: int, name: str, full_name: str, language: str, stats: RepositoryStats):
        super().__init__(name, full_name)
        self._id = id
        self._language = language
        self._stats = stats

    @property
    def id(self) -> int:
        return self._id

    @property
    def language(self) -> str:
        return self._language

    @property
    def stats(self) -> RepositoryStats:
        return self._stats

    def __str__(self) -> str:
        return f"Репозиторий: id={self._id}, name={self._name}, full_name={self._full_name}, language={self._language}, stats=({self._stats})"
