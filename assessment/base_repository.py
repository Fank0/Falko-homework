class BaseRepository:
    def __init__(self, name: str, full_name: str):
        self._name = name
        self._full_name = full_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def full_name(self) -> str:
        return self._full_name

    def __str__(self) -> str:
        return f"BaseRepository: {self._name} ({self._full_name})"
