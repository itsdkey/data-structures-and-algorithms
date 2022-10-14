import random
from unittest import TestCase
from typing import Iterable

from ..quicksort import QuickSortLomuto, QuickSortHoare


class QuickSortLomutoTestCase(TestCase):
    """TestCase for the QuickSort algorithm with Lomuto partition scheme."""

    def test_1(self):
        testcases = [
            range(1, 20),
            range(1, 200),
            range(543, 56063),
        ]
        for testcase in testcases:
            with self.subTest(testcase=testcase):
                self._test(testcase)

    def _test(self, elements: Iterable) -> None:
        array = list(elements)
        random.shuffle(array)

        result = QuickSortLomuto().sort(array)

        self.assertEqual(result, [x for x in elements])


class QuickSortHoareTestCase(TestCase):
    """TestCase for the QuickSort algorithm with Lomuto partition scheme."""

    def test_1(self):
        testcases = [
            range(1, 8),
            range(1, 20),
            range(1, 200),
            range(543, 56063),
        ]
        for testcase in testcases:
            with self.subTest(testcase=testcase):
                array = list(testcase)
                random.shuffle(array)

                result = QuickSortHoare().sort(array)

                self.assertEqual(result, [x for x in testcase])

    def test_2(self):
        array = [7, 5, 2, 3, 1, 4, 6]
        expected_result = [1, 2, 3, 4, 5, 6, 7]

        result = QuickSortHoare().sort(array)

        self.assertEqual(result, expected_result)

    def test_3(self):
        array = [2, 4, 3, 2]
        expected_result = [2, 2, 3, 4]

        result = QuickSortHoare().sort(array)

        self.assertEqual(result, expected_result)

    def test_4(self):
        array = [2, 2]
        expected_result = [2, 2]

        result = QuickSortHoare().sort(array)

        self.assertEqual(result, expected_result)

    def test_5(self):
        array = [22, 11, 88, 66, 55, 77, 33, 44]
        expected_result = [11, 22, 33, 44, 55, 66, 77, 88]

        result = QuickSortHoare().sort(array)

        self.assertEqual(result, expected_result)

    def test_6(self):
        array = [20, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_result = [3, 4, 5, 6, 7, 8, 9, 10, 20]

        result = QuickSortHoare().sort(array)

        self.assertEqual(result, expected_result)
