from collections import deque


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
