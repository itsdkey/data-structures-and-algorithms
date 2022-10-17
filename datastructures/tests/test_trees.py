from unittest import TestCase

from ..trees import BinaryTreeNode


class BinaryTreeNodeTestCase(TestCase):
    """TestCase for BinaryTreeNode."""

    def setUp(self) -> None:
        values = [1, 10, 21, 33, 18, 3, 128, 25, None, None, 300, None, None, 5, 82]
        self.root = self.create_tree(values)

    @staticmethod
    def create_tree(values: list) -> BinaryTreeNode:
        root = BinaryTreeNode(values[0])
        stack = [root]
        for index, value in enumerate(values[1:]):
            parent = stack[0]
            if value is not None:
                if index % 2 == 0:
                    node = parent.insert_left(value)
                else:
                    node = parent.insert_right(value)
                stack.append(node)
            if index and index % 2:
                stack.pop(0)
        return root

    def test_inorder(self):
        # expected_value = [33, 10, 18, 1, 3, 21, 128]
        expected_value = [25, 33, 10, 18, 300, 1, 3, 21, 5, 128, 82]

        result = self.root.get_inorder()

        self.assertEqual(expected_value, result)

    def test_preorder(self):
        # expected_value = [1, 10, 33, 18, 21, 3, 128]
        expected_value = [1, 10, 33, 25, 18, 300, 21, 3, 128, 5, 82]

        result = self.root.get_preorder()

        self.assertEqual(expected_value, result)

    def test_postorder(self):
        # expected_value = [33, 18, 10, 3, 128, 21, 1]
        expected_value = [25, 33, 300, 18, 10, 3, 5, 82, 128, 21, 1]

        result = self.root.get_postorder()

        self.assertEqual(expected_value, result)

    def test_breadth_first_search_finds_value(self):
        expected_path = [1, 10, 21, 33, 18]

        found, path = self.root.breadth_first_search(18)

        self.assertTrue(found)
        self.assertEqual(expected_path, path)

    def test_breadth_first_search_doesnt_find_value(self):
        expected_path = [1, 10, 21, 33, 18, 3, 128, 25, 300, 5, 82]

        found, path = self.root.breadth_first_search(180)

        self.assertFalse(found)
        self.assertEqual(expected_path, path)

    def test_depth_first_search_finds_value(self):
        expected_path = [1, 10, 33, 25, 18]

        found, path = self.root.depth_first_search(18)

        self.assertTrue(found)
        self.assertEqual(expected_path, path)

    def test_depth_first_search_doesnt_find_value(self):
        expected_path = [1, 10, 33, 25, 18, 300, 21, 3, 128, 5, 82]

        found, path = self.root.depth_first_search(180)

        self.assertFalse(found)
        self.assertEqual(expected_path, path)
