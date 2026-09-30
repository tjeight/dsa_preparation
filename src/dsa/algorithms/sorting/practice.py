class SortingAlgorithms:
    def selection_sort(self, numbers: list[int]) -> list[int]:

        length: int = len(numbers)

        if length <= 1:
            return numbers

        for i in range(length - 2):
            min_index = i
            for j in range(i + 1, length):
                if numbers[j] < numbers[min_index]:
                    min_index = j

            if i != min_index:
                numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

        return numbers

    def bubble_sort(self, numbers: list[int]):
        length: int = len(numbers)
        if length <= 1:
            return numbers

        for i in range(length):
            for j in range(length - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        return numbers

    def insertion_sort(self, numbers: list[int]):

        length: int = len(numbers)

        if length <= 1:
            return numbers

        for i in range(length):
            key = numbers[i]
            j = i - 1

            while j >= 0 and numbers[j] > key:
                numbers[j + 1] = numbers[j]
                j -= 1

            numbers[j + 1] = key

        return numbers

    def merge_sort(self, numbers: list[int]) -> list[int]:
        if len(numbers) <= 1:
            return numbers

        # divide from the middle
        middle: int = len(numbers) // 2

        left = numbers[:middle]
        right = numbers[middle:]

        left: list[int] = self.merge_sort(left)
        right: list[int] = self.merge_sort(right)

        # Sorting logic
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def quick_sort(self, numbers: list[int]) -> list[int]:
        if len(numbers) <= 1:
            return numbers

        pivot = numbers[-1]

        i = -1
        for j in range(len(numbers) - 1):
            if numbers[j] < pivot:
                i = i + 1
                numbers[i], numbers[j] = numbers[j], numbers[i]

        # Swap the pivot
        numbers[i + 1], numbers[-1] = numbers[-1], numbers[i + 1]

        pivot_index = i + 1

        left = numbers[:pivot_index]
        right = numbers[pivot_index + 1 :]

        # Sort the before the pivot and after the pivot recursively

        left = self.quick_sort(numbers=numbers[:pivot_index])
        right = self.quick_sort(numbers=numbers[pivot_index + 1 :])

        # Combine the sorted left partition, pivot, and sorted right partition
        return left + [pivot] + right
