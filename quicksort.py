import random

def randomized_quicksort(arr):
    """
    Sorts an array using Randomized Quicksort.
    A pivot is chosen uniformly at random from the array.

    Time Complexity:
        Average Case: O(n log n)
        Worst Case: O(n^2) (very unlikely due to randomization)

    Handles:
        - Empty arrays
        - Arrays with duplicate values
        - Already sorted arrays
    """

    # Base case: arrays of size 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr

    # Choose a random pivot index
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Partition the array into three parts
    left = []     # Elements smaller than pivot
    middle = []   # Elements equal to pivot
    right = []    # Elements greater than pivot

    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            middle.append(element)

    # Recursively sort left and right partitions
    return randomized_quicksort(left) + middle + randomized_quicksort(right)


def deterministic_quicksort(arr):
    """
    Sorts an array using Deterministic Quicksort.
    The first element is always chosen as the pivot.

    Time Complexity:
        Best/Average Case: O(n log n)
        Worst Case: O(n^2) (for sorted or reverse-sorted input)
    """

    # Base case
    if len(arr) <= 1:
        return arr

    # Always choose the first element as pivot
    pivot = arr[0]

    # Partition remaining elements
    left = []
    right = []

    for element in arr[1:]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)

    # Recursively sort partitions
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)
