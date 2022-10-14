from unittest import TestCase

from ..hashmaps import BasicHashMap, AdvancedHashMap


class BasicHashMapTestCase(TestCase):
    """TestCase for the BasicHashMap class which implements public
    methods for accessing/inserting/deleting values."""

    def setUp(self) -> None:
        self.custom_dict = BasicHashMap()

    def test_insert(self):
        key = 'test'
        expected_value = 123
        hashed_key = 8

        self.custom_dict.insert(key, expected_value)

        self.assertEqual(self.custom_dict.values[hashed_key], expected_value)

    def test_get(self):
        key = 'test'
        expected_value = 123
        self.custom_dict.insert(key, expected_value)

        value = self.custom_dict.get(key)

        self.assertEqual(value, expected_value)

    def test_delete(self):
        key = 'test'
        expected_value = 123
        hashed_key = 8
        self.custom_dict.insert(key, expected_value)

        self.custom_dict.delete(key)

        self.assertIsNone(self.custom_dict.values[hashed_key])


class AdvancedHashMapTestCase(TestCase):
    """TestCase for the AdvancedHashMap class which implements magic
    methods for accessing/inserting/deleting values."""

    def setUp(self) -> None:
        self.custom_dict = BasicHashMap()

    def test_insert(self):
        key = 'test'
        expected_value = 123
        hashed_key = 8

        self.custom_dict.insert(key, expected_value)

        self.assertEqual(self.custom_dict.values[hashed_key], expected_value)

    def test_get(self):
        key = 'test'
        expected_value = 123
        self.custom_dict.insert(key, expected_value)

        value = self.custom_dict.get(key)

        self.assertEqual(value, expected_value)

    def test_delete(self):
        key = 'test'
        expected_value = 123
        hashed_key = 8
        self.custom_dict.insert(key, expected_value)

        self.custom_dict.delete(key)

        self.assertIsNone(self.custom_dict.values[hashed_key])