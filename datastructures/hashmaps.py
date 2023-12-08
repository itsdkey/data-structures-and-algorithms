from typing import Any


class BasicHashTable:
    """A custom class implementing simple logic of a hashtable.

    It uses public methods for lookup/insert/delete operations. It doesn't
    handle collisions.
    """

    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.items = [None for x in range(self.size)]

    def _hash(self, key: str) -> int:
        if not isinstance(key, str):
            raise KeyError(f"{key} is not a string!")

        _sum = sum(ord(x) for x in key)
        _sum %= self.size
        return _sum

    def insert(self, key: str, value: Any) -> None:
        hashed_key = self._hash(key)
        self.items[hashed_key] = value

    def get(self, key: str) -> Any:
        hashed_key = self._hash(key)
        return self.items[hashed_key]

    def delete(self, key: str) -> None:
        hashed_key = self._hash(key)
        self.items[hashed_key] = None


class AdvancedHashTable:
    """A custom class implementing simple logic of a hashtable.

    It uses magic methods for lookup/insert/delete operations. It doesn't handle
    collisions.
    """

    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.items = [None for x in range(self.size)]

    def _hash(self, key: str) -> int:
        if not isinstance(key, str):
            raise KeyError(f"{key} is not a string!")

        _sum = sum(ord(x) for x in key)
        _sum %= self.size
        return _sum

    def __setitem__(self, key: str, value: Any) -> None:
        hashed_key = self._hash(key)
        self.items[hashed_key] = value

    def __getitem__(self, key: str) -> Any:
        hashed_key = self._hash(key)
        return self.items[hashed_key]

    def __delitem__(self, key: str) -> None:
        hashed_key = self._hash(key)
        self.items[hashed_key] = None


class RealHashTable:
    """A custom class implementing simple logic of a hashtable.

    It stores triplets [hash, key, value] under a certain index (the hash
    value).

    This is a basic implementation of Python dict till 3.6. It doesn't handle
    collisions.
    """

    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.items = [[] for x in range(self.size)]

    def _hash(self, key: str) -> int:
        if not isinstance(key, str):
            raise KeyError(f"{key} is not a string!")

        _sum = sum(ord(x) for x in key)
        _sum %= self.size
        return _sum

    def __setitem__(self, key: str, value: Any) -> None:
        hashed_key = self._hash(key)
        self.items[hashed_key] = [hashed_key, key, value]

    def __getitem__(self, key: str) -> Any:
        hashed_key = self._hash(key)
        return self.items[hashed_key][2]

    def __delitem__(self, key: str) -> None:
        hashed_key = self._hash(key)
        self.items[hashed_key].clear()


class RealOrderedHashTable:
    """A custom class implementing simple logic of a hashtable.

    Compact array:
        It stores triplets [hash, key, value] in order of insertion.
    Sparse array:
        It stores indexes to compact array. The place is defined by the hashed key.

    This is a basic implementation of Python dict 3.6+.

    It doesn't handle collisions.

    Based on:
    https://www.pypy.org/posts/2015/01/faster-more-memory-efficient-and-more-4096950404745375390.html
    """

    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.compact_array = [[] for _ in range(self.size)]
        self.sparse_array = [None for _ in range(self.size)]
        self.num_items = 0

    def _hash(self, key: str) -> int:
        if not isinstance(key, str):
            raise KeyError(f"{key} is not a string!")

        _sum = sum(ord(x) for x in key)
        _sum %= self.size
        return _sum

    def __setitem__(self, key: str, value: Any) -> None:
        hashed_key = self._hash(key)
        self.compact_array[self.num_items] = [hashed_key, key, value]
        self.sparse_array[hashed_key] = self.num_items
        self.num_items += 1

    def __getitem__(self, key: str) -> Any:
        hashed_key = self._hash(key)
        index = self.sparse_array[hashed_key]
        return self.compact_array[index][2]

    def __delitem__(self, key: str) -> None:
        hashed_key = self._hash(key)
        index = self.sparse_array[hashed_key]
        self.compact_array[index].clear()
        self.sparse_array[hashed_key] = None


class HashTableWithChaining:
    """A custom class implementing simple logic of a hashtable.

    It handles collisions.
    It also handles KeyErrors and Storing None values.

    Based on:
    https://youtu.be/54iv1si4YCM
    """

    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.items = [[] for _ in range(self.size)]

    def _hash(self, key: str) -> int:
        if not isinstance(key, str):
            raise KeyError(f"{key} is not a string!")

        _sum = sum(ord(x) for x in key)
        _sum %= self.size
        return _sum

    def __setitem__(self, key: str, value: Any) -> None:
        hashed_key = self._hash(key)
        triplet = (hashed_key, key, value)
        update = False
        for index, element in enumerate(self.items[hashed_key]):
            if element[1] == key:
                self.items[hashed_key][index] = triplet
                update = True
                break
        if not update:
            self.items[hashed_key].append(triplet)

    def __getitem__(self, key: str) -> Any:
        hashed_key = self._hash(key)
        for index, element in enumerate(self.items[hashed_key]):
            if element[1] == key:
                return element[2]
        raise KeyError(f'"{key}" not in storage!')

    def __delitem__(self, key: str) -> None:
        hashed_key = self._hash(key)
        for index, element in enumerate(self.items[hashed_key]):
            if element[1] == key:
                del self.items[hashed_key][index]
