from unittest import TestCase

from ..hashmaps import (
    AdvancedHashTable,
    BasicHashTable,
    HashTableWithChaining,
    RealHashTable,
    RealOrderedHashTable,
)


class BasicHashTableTestCase(TestCase):
    """TestCase for the BasicHashTable class which implements public methods for
    accessing/inserting/deleting values."""

    def setUp(self) -> None:
        self.custom_dict = BasicHashTable()

    def test_insert(self):
        key = "test"
        expected_value = 123
        hashed_key = 0

        self.custom_dict.insert(key, expected_value)

        self.assertEqual(self.custom_dict.items[hashed_key], expected_value)

    def test_get(self):
        key = "test"
        expected_value = 123
        self.custom_dict.insert(key, expected_value)

        value = self.custom_dict.get(key)

        self.assertEqual(value, expected_value)

    def test_delete(self):
        key = "test"
        expected_value = 123
        hashed_key = 0
        self.custom_dict.insert(key, expected_value)

        self.custom_dict.delete(key)

        self.assertIsNone(self.custom_dict.items[hashed_key])


class AdvancedHashTableTestCase(TestCase):
    """TestCase for the AdvancedHashTable class which implements magic methods
    for accessing/inserting/deleting values."""

    def setUp(self) -> None:
        self.custom_dict = AdvancedHashTable()

    def test_insert(self):
        key = "test"
        expected_value = 123
        hashed_key = 0

        self.custom_dict[key] = expected_value

        self.assertEqual(self.custom_dict.items[hashed_key], expected_value)

    def test_get(self):
        key = "test"
        expected_value = 123
        self.custom_dict[key] = expected_value

        value = self.custom_dict[key]

        self.assertEqual(value, expected_value)

    def test_delete(self):
        key = "test"
        expected_value = 123
        hashed_key = 0
        self.custom_dict[key] = expected_value

        del self.custom_dict[key]

        self.assertIsNone(self.custom_dict.items[hashed_key])


class RealHashTableTestCase(TestCase):
    """TestCase for the RealHashTable class which implements magic methods for
    accessing/inserting/deleting values."""

    def setUp(self) -> None:
        self.custom_dict = RealHashTable()

    def test_insert(self):
        key = "test"
        value = 123
        hashed_key = 0
        expected_value = [hashed_key, key, value]

        self.custom_dict[key] = value

        self.assertEqual(self.custom_dict.items[hashed_key], expected_value)

    def test_get(self):
        key = "test"
        expected_value = 123
        self.custom_dict[key] = expected_value

        value = self.custom_dict[key]

        self.assertEqual(value, expected_value)

    def test_delete(self):
        key = "test"
        expected_value = 123
        hashed_key = 0
        self.custom_dict[key] = expected_value
        expected_value = []

        del self.custom_dict[key]

        self.assertEqual(self.custom_dict.items[hashed_key], expected_value)


class RealOrderedHashTableTestCase(TestCase):
    """TestCase for the RealOrderedHashTable class which implements magic
    methods for accessing/inserting/deleting values."""

    def setUp(self) -> None:
        self.custom_dict = RealOrderedHashTable()

    def test_insert(self):
        key = "test"
        value = 123
        hashed_key = 0
        expected_value = [hashed_key, key, value]

        self.custom_dict[key] = value

        self.assertEqual(self.custom_dict.sparse_array[hashed_key], 0)
        self.assertEqual(self.custom_dict.compact_array[0], expected_value)

    def test_get(self):
        key = "test"
        expected_value = 123
        self.custom_dict[key] = expected_value

        value = self.custom_dict[key]

        self.assertEqual(value, expected_value)

    def test_delete(self):
        key = "test"
        expected_value = 123
        hashed_key = 0
        self.custom_dict[key] = expected_value
        expected_value = []

        del self.custom_dict[key]

        self.assertEqual(self.custom_dict.compact_array[hashed_key], expected_value)


class HashTableWithChainingTestCase(TestCase):
    """TestCase for the HashTableWithChaining class which implements magic
    methods for accessing/inserting/deleting values.

    It also handles collisions using chaining.
    """

    def setUp(self) -> None:
        self.custom_dict = HashTableWithChaining()

    def test_insert_one_key(self):
        triplets = [(0, "test", 123)]

        for triplet in triplets:
            self.custom_dict[triplet[1]] = triplet[2]

        self.assertEqual(self.custom_dict.items[0], triplets)

    def test_insert_key_with_none_value(self):
        triplets = [(0, "test", None)]

        for triplet in triplets:
            self.custom_dict[triplet[1]] = triplet[2]

        self.assertEqual(self.custom_dict.items[0], triplets)

    def test_insert_conflicting_keys(self):
        triplets = [
            (0, "test", 123),
            (0, "cccf1", 418),
        ]

        for triplet in triplets:
            self.custom_dict[triplet[1]] = triplet[2]

        self.assertEqual(self.custom_dict.items[0], triplets)

    def test_raises_KeyError_when_key_not_in_storage(self):
        with self.assertRaises(KeyError):
            _ = self.custom_dict["missing key"]

    def test_get_normal_key(self):
        triplets = [
            (0, "test", 123),
            (0, "cccf1", 418),
        ]
        for triplet in triplets:
            self.custom_dict[triplet[1]] = triplet[2]
        expected_value = 123

        value = self.custom_dict["test"]

        self.assertEqual(value, expected_value)

    def test_get_key_with_none_value(self):
        triplets = [
            (0, "test", None),
        ]
        for triplet in triplets:
            self.custom_dict[triplet[1]] = triplet[2]

        value = self.custom_dict["test"]

        self.assertIsNone(value)

    def test_delete(self):
        triplets = [
            (0, "test", 123),
            (0, "cccf1", 418),
        ]
        for triplet in triplets:
            self.custom_dict[triplet[1]] = triplet[2]
        expected_value = [(0, "cccf1", 418)]

        del self.custom_dict["test"]

        self.assertEqual(self.custom_dict.items[0], expected_value)
