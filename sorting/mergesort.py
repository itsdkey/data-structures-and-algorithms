class MergeSort:
    """
    Merge sort algorithm based on:

    https://youtu.be/cVZMah9kEjI
    https://en.wikipedia.org/wiki/Merge_sort#Top-down_implementation
    """
    def sort(self, elements: list) -> list:
        return self.divide(elements)

    def divide(self, elements: list):
        length = len(elements)
        if length == 1:
            return elements

        middle = length // 2
        left, right = elements[:middle], elements[middle:]
        # print(f'{left=}, {right=}')

        left = self.divide(left)
        right = self.divide(right)

        merged = self.merge(left, right)
        # print(f'{merged=}')

        return merged

    @staticmethod
    def merge(left: list, right: list) -> list:
        left_index, right_index, current_index = (0, 0, 0)
        merged = []
        while left_index < len(left) and right_index < len(right):
            left_value = left[left_index]
            right_value = right[right_index]
            if left_value < right_value:
                merged.append(left_value)
                left_index += 1
            else:
                merged.append(right_value)
                right_index += 1

        if left_index < len(left):
            merged.extend(left[left_index:])

        if right_index < len(right):
            merged.extend(right[right_index:])

        return merged
