from typing import Any


class BasicHashMap:
    """
    A custom class implementing simple logic of a hashtable/hashmap.

    It uses public methods for lookup/insert/delete operations.
    """

    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.values = [None for x in range(self.size)]

    def _hash(self, key: str) -> int:
        if not isinstance(key, str):
            raise KeyError(f'{key} is not a string!')

        _sum = sum([ord(x) for x in key])
        _sum %= self.size
        return _sum

    def insert(self, key: str, value: Any) -> None:
        hashed_key = self._hash(key)
        self.values[hashed_key] = value

    def get(self, key: str) -> Any:
        hashed_key = self._hash(key)
        return self.values[hashed_key]

    def delete(self, key: str) -> None:
        hashed_key = self._hash(key)
        self.values[hashed_key] = None


class AdvancedHashMap:
    ...