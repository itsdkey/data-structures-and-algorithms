from unittest import TestCase

from quadrocopter.dataclasses import Point
from quadrocopter.quadrocopter import Quadrocopter


class QuadrocopterTestCase(TestCase):
    """TestCase for the Quadrocopter class."""

    def test_1_returns_true(self):
        antennas = [
            Point(6, 11, 4),
            Point(8, 17, 3),
            Point(19, 19, 2),
            Point(19, 11, 4),
            Point(15, 7, 6),
            Point(12, 19, 4),
        ]
        start_point = Point(10, 19)
        end_point = Point(19, 14)
        expected_result = "bezpieczny przelot jest możliwy"

        result = Quadrocopter(antennas, start_point, end_point).calculate()

        self.assertEqual(result, expected_result)

    def test_2_returns_true(self):
        antennas = [
            Point(2, 2, 1),
            Point(2, 4, 1),
            Point(4, 2, 1),
            Point(4, 4, 1),
        ]
        start_point = Point(2, 2)
        end_point = Point(4, 4)
        expected_result = "bezpieczny przelot jest możliwy"

        result = Quadrocopter(antennas, start_point, end_point).calculate()

        self.assertEqual(result, expected_result)

    def test_2_returns_true_when_antennas_inside_themselves(self):
        antennas = [
            Point(2, 2, 1),
            Point(2, 2, 2),
            Point(2, 2, 3),
            Point(2, 2, 4),
        ]
        start_point = Point(2, 2)
        end_point = Point(2, 6)
        expected_result = "bezpieczny przelot jest możliwy"

        result = Quadrocopter(antennas, start_point, end_point).calculate()

        self.assertEqual(result, expected_result)

    def test_3_returns_false(self):
        antennas = [
            Point(2, 2, 1),
            Point(2, 5, 1),
            Point(5, 2, 1),
            Point(5, 5, 1),
        ]
        start_point = Point(2, 2)
        end_point = Point(5, 5)
        expected_result = "bezpieczny przelot nie jest możliwy"

        result = Quadrocopter(antennas, start_point, end_point).calculate()

        self.assertEqual(result, expected_result)

    def test_returns_false_when_start_point_outside_antennas(self):
        antennas = [
            Point(2, 2, 1),
            Point(2, 5, 1),
            Point(5, 2, 1),
            Point(5, 5, 1),
        ]
        start_point = Point(7, 7)
        end_point = Point(5, 5)
        expected_result = "bezpieczny przelot nie jest możliwy"

        result = Quadrocopter(antennas, start_point, end_point).calculate()

        self.assertEqual(result, expected_result)

    def test_returns_false_when_end_point_outside_antennas(self):
        antennas = [
            Point(2, 2, 1),
            Point(2, 5, 1),
            Point(5, 2, 1),
            Point(5, 5, 1),
        ]
        start_point = Point(2, 2)
        end_point = Point(7, 7)
        expected_result = "bezpieczny przelot nie jest możliwy"

        result = Quadrocopter(antennas, start_point, end_point).calculate()

        self.assertEqual(result, expected_result)
