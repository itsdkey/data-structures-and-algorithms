from __future__ import annotations

from collections import deque
from typing import Optional


class BinaryTreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.value}] left: {self.left}, right: {self.right}"

    def insert_left(self, value: int):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value: int):
        self.right = BinaryTreeNode(value)
        return self.right

    def get_inorder(self) -> list:
        """First left, then parent, then right."""
        result = []
        if self.left:
            result.extend(self.left.get_inorder())
        result.append(self.value)
        if self.right:
            result.extend(self.right.get_inorder())
        return result

    def get_preorder(self) -> list:
        """First parent, then left, then right."""
        result = [self.value]
        if self.left:
            result.extend(self.left.get_preorder())
        if self.right:
            result.extend(self.right.get_preorder())
        return result

    def get_postorder(self) -> list:
        """First left, then right, then parent."""
        result = []
        if self.left:
            result.extend(self.left.get_postorder())
        if self.right:
            result.extend(self.right.get_postorder())
        result.append(self.value)
        return result

    def breadth_first_search(self, value: int) -> tuple[bool, list[int]]:
        path = []
        stack = deque([self])
        while len(stack) > 0:
            node = stack.popleft()
            path.append(node.value)
            if node.value == value:
                return True, path
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False, path

    def depth_first_search(self, value: int) -> tuple[bool, list[int]]:
        """Depth-first search using pre-order traversal."""
        path = [self.value]
        if self.value == value:
            return True, path
        if self.left:
            found, traversed_path = self.left.depth_first_search(value)
            path.extend(traversed_path)
            if found:
                return found, path
        if self.right:
            found, traversed_path = self.right.depth_first_search(value)
            path.extend(traversed_path)
            if found:
                return found, path
        return False, path


class BinarySearchTreeNode(BinaryTreeNode):
    def insert_left(self, value: int):
        raise NotImplementedError(
            f"{self.__class__.__name__} does not allow manual insertion!"
            f" Use .insert() method."
        )

    def insert_right(self, value: int):
        raise NotImplementedError(
            f"{self.__class__.__name__} does not allow manual insertion!"
            f" Use .insert() method."
        )

    def insert(self, value: int):
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTreeNode(value)

        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)

    def depth_first_search(self, value: int) -> tuple[bool, list[int]]:
        """Depth-first search using recursive binary search algorithm."""
        found, path = False, [self.value]
        if self.value == value:
            return True, path
        if value < self.value:
            if self.left:
                found, traversed_path = self.left.depth_first_search(value)
                path.extend(traversed_path)
            else:
                return False, path
        if value > self.value:
            if self.right:
                found, traversed_path = self.right.depth_first_search(value)
                path.extend(traversed_path)
            else:
                return False, path
        return found, path

    def depth_first_search_iterative(self, value: int) -> tuple[bool, list]:
        """Depth-first search using iterative binary search algorithm."""
        node = self
        path = []
        while node is not None:
            path.append(node)
            if node.value == value:
                break
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
        if node:
            return True, path
        return False, path

    def delete(self, value: int, parent=None):
        """Delete a node from the tree."""
        found, path = self.depth_first_search_iterative(value)
        if not found:
            raise ValueError(f"{value} not in Tree")
        if len(path) == 1:
            parent, node = parent, path[0]
        else:
            parent, node = path[-2:]

        # leaf node
        if not any([node.left, node.right]):
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            del node
        # single child
        elif (node.left and not node.right) or (not node.left and node.right):
            if parent.left == node:
                parent.left = node.left if node.left else node.right
            elif parent.right == node:
                parent.right = node.right if node.right else node.left
            del node
        # two children
        else:
            smallest_node = node.right.find_minimum()
            node.value = smallest_node.value
            node.right.delete(smallest_node.value, node)

    def find_minimum(self):
        if self.left:
            return self.left.find_minimum()
        return self


class AVLTreeNode:
    """Class representing an AVL Tree.

    Based on:
    https://youtu.be/vRwi_UcZGjU
    https://backtobackswe.com/platform/content/avl-trees-rotations/solutions
    """

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.height: int = 0
        self.left: Optional[AVLTreeNode] = None
        self.right: Optional[AVLTreeNode] = None

    def create_tree(self, items: list, threshold: int) -> None:
        if not items:
            return

        root = items[0]
        for index in range(1, len(items)):  # omit slicing so we don't iterate twice
            self.insert(root, items[index], threshold)

    def insert(self, node: AVLTreeNode, value: int, threshold: int) -> AVLTreeNode:
        # return a child when we find a empty spot
        # (refactor of BinarySearchTreeNode.insert else statements)
        if not node:
            return AVLTreeNode(value)

        if value <= node.value:
            node.left = node.left.insert(node.left, value, threshold)
        else:
            node.right = node.right.insert(node.right, value, threshold)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > threshold:
            # left heavy - positive balance
            if self.get_balance(node.left) >= 0:
                # left node is left heavy ->
                # only rotate right
                node = self.rotate_right(node)
            else:
                # left node is right heavy ->
                # rotate left then right (left_right rotation)
                node = self.rotate_left_right(node)
        elif balance < -threshold:
            # right heavy - negative balance
            if self.get_balance(node.right) <= 0:
                # right node is right heavy ->
                # rotate left
                node = self.rotate_left(node)
            else:
                # right node is left heavy ->
                # rotate right then left (right_left rotation)
                node = self.rotate_right_left(node)
        return node

    @staticmethod
    def get_height(node: AVLTreeNode) -> int:
        """Return height of a subtree if it exists."""
        if not node:
            return 0
        return node.height

    def get_balance(self, node: AVLTreeNode):
        """Return the balance of a node's subtrees.

        positives - left heavy (left side is taller than right)
        0 - full balanced
        negatives - right heavy (right side is taller than left)
        """
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, node: AVLTreeNode) -> AVLTreeNode:
        """Rotate right and return root of the subtree."""
        child = node.left
        node.left = child.right
        child.right = node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        child.height = 1 + max(self.get_height(child.left), node.height)
        return child

    def rotate_left(self, node: AVLTreeNode) -> AVLTreeNode:
        """Rotate left and return root of the subtree."""
        child = node.right
        node.right = child.left
        child.left = node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        child.height = 1 + max(self.get_height(child.left), node.height)
        return child

    def rotate_left_right(self, node: AVLTreeNode) -> AVLTreeNode:
        """Rotate left then right."""
        node.left = self.rotate_left(node.left)
        return self.rotate_right(node)

    def rotate_right_left(self, node: AVLTreeNode) -> AVLTreeNode:
        """Rotate right then left."""
        node.right = self.rotate_right(node.right)
        return self.rotate_left(node)
