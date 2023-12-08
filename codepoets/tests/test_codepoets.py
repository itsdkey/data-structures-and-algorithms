from unittest import TestCase

from codepoets.tasks import task2


class Task2TestCase(TestCase):
    """TestCase for the task2."""

    def setUp(self) -> None:
        self.task = task2

    def test_foo(self):
        values = [
            {
                "name": "library_1",
                "softs": {
                    "computer_1": ["1.0.0", "1.0.1", "1.1.0"],
                    "computer_2": ["0.2.0", "0.2.1", "0.2.3"],
                    "computer_3": ["2.2.0"],
                },
            },
            {
                "name": "library_2",
                "softs": {
                    "computer_1": ["1.1.5"],
                    "computer_3": ["0.2.0", "0.2.1", "0.2.3"],
                    "computer_4": ["2.2.0", "2.2.1"],
                },
            },
            {
                "name": "library_3",
                "softs": {
                    "computer_1": ["1.1.5"],
                    "computer_4": ["2.2.0", "2.2.1", "2.2.3"],
                    "computer_5": ["2.2.0", "2.2.1"],
                    "computer_6": ["6.1.0", "6.2.1"],
                },
            },
        ]
        expected_result = {
            "computer_1": {"1.0.0", "1.0.1", "1.1.0", "1.1.5"},
            "computer_2": {"0.2.0", "0.2.1", "0.2.3"},
            "computer_3": {"2.2.0", "0.2.0", "0.2.1", "0.2.3"},
            "computer_4": {"2.2.0", "2.2.1", "2.2.3"},
            "computer_5": {"2.2.0", "2.2.1"},
            "computer_6": {"6.1.0", "6.2.1"},
        }

        result = self.task(values)

        self.assertDictEqual(result, expected_result)
