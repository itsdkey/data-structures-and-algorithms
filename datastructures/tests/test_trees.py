from unittest import TestCase

from ..trees import BinarySearchTreeNode, BinaryTreeNode


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
        expected_value = [25, 33, 10, 18, 300, 1, 3, 21, 5, 128, 82]

        result = self.root.get_inorder()

        self.assertEqual(expected_value, result)

    def test_preorder(self):
        expected_value = [1, 10, 33, 25, 18, 300, 21, 3, 128, 5, 82]

        result = self.root.get_preorder()

        self.assertEqual(expected_value, result)

    def test_postorder(self):
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


class BinarySearchTreeNodeTestCase(TestCase):
    """TestCase for BinarySearchTreeNode."""

    def setUp(self) -> None:
        values = [18, 12, 30, 10, 15, 28, 45, 1, 11, 14, 16, 20, 29, 40, 60]
        self.root = self.create_tree(values)

    @staticmethod
    def create_tree(values: list) -> BinarySearchTreeNode:
        root = BinarySearchTreeNode(values[0])
        for value in values[1:]:
            root.insert(value)
        return root

    def test_inorder(self):
        expected_order = [1, 10, 11, 12, 14, 15, 16, 18, 20, 28, 29, 30, 40, 45, 60]

        result = self.root.get_inorder()

        self.assertEqual(expected_order, result)

    def test_preorder(self):
        expected_order = [18, 12, 10, 1, 11, 15, 14, 16, 30, 28, 20, 29, 45, 40, 60]

        result = self.root.get_preorder()

        self.assertEqual(expected_order, result)

    def test_postorder(self):
        expected_order = [1, 11, 10, 14, 16, 15, 12, 20, 29, 28, 40, 60, 45, 30, 18]

        result = self.root.get_postorder()

        self.assertEqual(expected_order, result)

    def test_breadth_first_search_finds_value(self):
        expected_path = [18, 12, 30, 10, 15]

        found, path = self.root.breadth_first_search(15)

        self.assertTrue(found)
        self.assertEqual(expected_path, path)

    def test_breadth_first_search_doesnt_find_value(self):
        expected_path = [18, 12, 30, 10, 15, 28, 45, 1, 11, 14, 16, 20, 29, 40, 60]

        found, path = self.root.breadth_first_search(180)

        self.assertFalse(found)
        self.assertEqual(expected_path, path)

    def test_depth_first_search_finds_value(self):
        expected_path = [18, 12, 15]

        found, path = self.root.depth_first_search(15)

        self.assertTrue(found)
        self.assertEqual(expected_path, path)

    def test_depth_first_search_doesnt_find_value(self):
        expected_path = [18, 12, 15, 16]

        found, path = self.root.depth_first_search(17)

        self.assertFalse(found)
        self.assertEqual(expected_path, path)

    def test_depth_first_search_iterative_finds_value(self):
        expected_path = [18, 12, 15]

        found, path = self.root.depth_first_search_iterative(15)

        self.assertTrue(found)
        self.assertEqual(expected_path, [n.value for n in path])

    def test_depth_first_search_iterative_doesnt_find_value(self):
        expected_path = [18, 12, 15, 16]

        found, path = self.root.depth_first_search_iterative(17)

        self.assertFalse(found)
        self.assertEqual(expected_path, [n.value for n in path])

    def test_delete_leaf_node(self):
        expected_order = [1, 10, 12, 14, 15, 16, 18, 20, 28, 29, 30, 40, 45, 60]

        self.root.delete(11)

        result = self.root.get_inorder()
        self.assertEqual(expected_order, result)

    def test_delete_node_with_one_child(self):
        values = [18, 12, 30, 10, 15, 28, 45, 1, 11, 14, 16, 20, 29, 40]
        root = self.create_tree(values)
        expected_order = [1, 10, 11, 12, 14, 15, 16, 18, 20, 28, 29, 30, 40]

        root.delete(45)

        result = root.get_inorder()
        self.assertEqual(expected_order, result)

    def test_delete_node_with_two_children(self):
        expected_order = [1, 10, 11, 12, 14, 16, 18, 20, 28, 29, 30, 40, 45, 60]

        self.root.delete(15)

        result = self.root.get_inorder()
        self.assertEqual(expected_order, result)
