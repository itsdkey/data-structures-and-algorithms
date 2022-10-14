import random
from unittest import TestCase
from typing import Iterable

from ..mergesort import MergeSort


class MergeSortTestCase(TestCase):
    """TestCase for the MergeSort algorithm."""

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

        result = MergeSort().sort(array)

        self.assertEqual(result, [x for x in elements])
