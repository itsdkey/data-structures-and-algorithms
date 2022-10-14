class QuickSortLomuto:
    """
    Quicksort using Lomuto partition scheme.

    Source:
    https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
    """

    def sort(self, elements: list) -> list:
        # print(f'{elements=}')
        return self.quicksort(elements, 0, len(elements) - 1)

    def quicksort(self, elements: list, left_index: int, right_index: int) -> list:
        if left_index >= right_index or left_index < 0:
            return elements

        pivot_index = self.partition(elements, left_index, right_index)

        self.quicksort(elements, left_index, pivot_index - 1)
        # print(f'sorted left: {elements}')
        self.quicksort(elements, pivot_index, right_index)
        # print(f'sorted right: {elements}')
        return elements

    @staticmethod
    def partition(elements: list, low: int, high: int) -> int:
        pivot = elements[high]
        # print(f'{pivot=}')

        i = low - 1
        for j in range(low, high):
            if elements[j] <= pivot:
                i += 1
                elements[j], elements[i] = elements[i], elements[j]

        i += 1
        elements[high], elements[i] = elements[i], elements[high]
        # print(f'pivot index = {i}')
        # print(f'{elements=}')
        return i


class QuickSortHoare:
    """
    Quicksort using Hoare partition scheme.

    Source:
    https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
    """

    counter = 0

    def sort(self, elements: list) -> list:
        # print(f'{elements=}')
        _sorted = self.quicksort(elements, 0, len(elements) - 1)
        # print(f'{self.counter=}')
        return _sorted

    def quicksort(self, elements: list, left_index: int, right_index: int) -> list:
        # print(f'{left_index=}, {right_index=}')
        self.counter += 1
        if 0 <= left_index < right_index:
            pivot_index = self.partition('last pivot', elements, left_index, right_index)

            self.quicksort(elements, left_index, pivot_index)
            # print(f'sorted left')
            self.quicksort(elements, pivot_index + 1, right_index)
            # print(f'sorted right')
        return elements

    def partition(self, strategy: str, elements: list, low: int, high: int) -> int:
        methods = {
            'middle pivot': self.partition_with_middle_element,
            'last pivot': self.partition_with_last_element,
        }
        return methods[strategy](elements, low, high)

    @staticmethod
    def partition_with_middle_element(elements: list, low: int, high: int) -> int:
        """
        Using middle element in sublist as pivot.
        Based on wiki:
        https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
        """
        pivot_index = (low + high) // 2
        pivot = elements[pivot_index]
        # print(f'{pivot_index=}, {pivot=}')

        left = low
        right = high

        while True:
            while elements[left] < pivot:
                left += 1
            while elements[right] > pivot:
                right -= 1

            if left >= right:
                return right

            if elements[left] == elements[right]:
                # when there are duplicates -> return pivot index
                # because we are sure it's in the right place
                return pivot_index

            # print(f'Swap elements {elements[left]} <-> {elements[right]}')
            elements[left], elements[right] = elements[right], elements[left]
            # print(f'{elements=}')

    @staticmethod
    def partition_with_last_element(elements: list, low: int, high: int) -> int:
        """
        Using last element in sublist as pivot.

        Based on: https://youtu.be/9KBwdDEwal8
        """
        pivot_index = high
        pivot = elements[pivot_index]
        # print(f'{pivot_index=}, {pivot=}')

        left = low
        right = high - 1

        while True:
            while elements[left] < pivot:
                left += 1
            while elements[right] >= pivot and right > low:
                right -= 1
            if left >= right:
                elements[left], elements[pivot_index] = elements[pivot_index], elements[left]
                return right
            # print(f'Swap elements {elements[left]} <-> {elements[right]}')
            elements[left], elements[right] = elements[right], elements[left]
            # print(f'{elements=}')
