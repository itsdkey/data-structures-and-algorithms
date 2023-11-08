from unittest import TestCase

from dropbox.solution import solution


class SolutionTestCase(TestCase):
    """TestCase for the Dropbox task I got."""

    def test_1(self):
        queries = [
            ["SET", "1", "employee1", "age", "20"],
            ["SET", "2", "employee2", "age", "30"],
            ["SET", "3", "employee1", "age", "40"],
            ["GET", "4", "employee1", "age"],
            ["GET", "5", "employee", "age"],
            ["GET", "6", "employee2", "age"],
        ]
        expected_output = ["", "", "", "40", "", "30"]

        result = solution(queries)

        self.assertEqual(result, expected_output)

    def test_2(self):
        queries = [
            ["SET", "1", "employee1", "age", "20"],
            ["SET", "2", "employee2", "age", "30"],
            ["COMPARE_AND_SET", "3", "employee1", "age", "40", "30"],
            ["COMPARE_AND_SET", "4", "employee1", "age", "20", "25"],
            ["COMPARE_AND_SET", "5", "employee1", "age", "40", "30"],
            ["GET", "6", "employee1", "age"],
        ]
        expected_output = ["", "", "false", "true", "false", "25"]

        result = solution(queries)

        self.assertEqual(result, expected_output)

    def test_3(self):
        queries = [
            ["SET", "1", "employee1", "age", "20"],
            ["SET", "2", "employee2", "age", "30"],
            ["COMPARE_AND_SET", "3", "employee1", "age", "40", "30"],
            ["COMPARE_AND_SET", "4", "employee1", "age", "20", "25"],
            ["COMPARE_AND_DELETE", "5", "employee1", "age", "25"],
            ["GET", "6", "employee1", "age"],
        ]
        expected_output = ["", "", "false", "true", "true", ""]

        result = solution(queries)

        self.assertEqual(result, expected_output)

    def test_4(self):
        queries = [
            ["SET", "1", "employee1", "age", "20"],
            ["SET", "2", "employee1", "weight", "100"],
            ["SET", "3", "employee1", "height", "180"],
            ["SET", "4", "employee1", "ax", "200"],
            ["COMPARE_AND_SET", "3", "employee1", "age", "40", "30"],
            ["COMPARE_AND_SET", "4", "employee1", "age", "20", "25"],
            ["SCAN", "5", "employee1"],
            ["SCAN_WITH_PREFIX", "6", "employee1", "a"],
        ]
        expected_output = [
            "",
            "",
            "",
            "",
            "false",
            "true",
            "age(25), ax(200), height(180), weight(100)",
            "age(25), ax(200)",
        ]

        result = solution(queries)

        self.assertEqual(result, expected_output)

    def test_5(self):
        queries = [
            ["SET", "1", "employee1", "age", "20"],
            ["SET_WITH_TTL", "2", "employee1", "weight", "100", "20"],
            ["GET", "20", "employee1", "age"],
            ["GET", "21", "employee1", "weight"],
            ["GET", "22", "employee1", "weight"],
            ["SCAN", "50", "employee1"],
        ]
        expected_output = ["", "", "20", "100", "", "age(20)"]

        result = solution(queries)

        self.assertEqual(result, expected_output)

    def test_6(self):
        queries = [
            ["SET", "1", "employee1", "age", "20"],
            ["SET_WITH_TTL", "2", "employee1", "age", "25", "30"],
            ["SET_WITH_TTL", "3", "employee1", "weight", "100", "20"],
            [
                "COMPARE_AND_SET_WITH_TTL",
                "20",
                "employee1",
                "weight",
                "100",
                "90",
                "20",
            ],
            [
                "COMPARE_AND_SET_WITH_TTL",
                "21",
                "employee1",
                "weight",
                "100",
                "90",
                "20",
            ],
            ["SCAN", "22", "employee1"],
            ["SCAN", "32", "employee1"],
            ["COMPARE_AND_SET_WITH_TTL", "39", "employee1", "weight", "90", "80", "20"],
            [
                "COMPARE_AND_SET_WITH_TTL",
                "60",
                "employee1",
                "weight",
                "100",
                "70",
                "20",
            ],
            ["SCAN", "61", "employee1"],
        ]
        expected_output = [
            "",
            "",
            "",
            "true",
            "false",
            "age(25), weight(90)",
            "weight(90)",
            "true",
            "false",
            "",
        ]

        result = solution(queries)

        self.assertEqual(result, expected_output)
