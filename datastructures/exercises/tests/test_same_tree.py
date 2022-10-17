from unittest import TestCase

from ..same_tree import Solution, TreeNode


class SameTreeTestCases(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_basic(self):
        p = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
        q = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
        expected_result = True

        result = self.solution.is_same_tree(p, q)

        self.assertEqual(expected_result, result)

    def test_1(self):
        p = TreeNode(1, left=TreeNode(1))
        q = TreeNode(1, left=None, right=TreeNode(1))
        expected_result = False

        result = self.solution.is_same_tree(p, q)

        self.assertEqual(expected_result, result)
