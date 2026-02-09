import time
import random
from quicksort import randomized_quicksort, deterministic_quicksort


def benchmark(sort_function, arr):
    """
    Measures execution time of a sorting function.

    Parameters:
        sort_function: sorting algorithm to test
        arr: input array

    Returns:
        Execution time in seconds
    """
    start_time = time.time()
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time


def generate_test_cases(n):
    """
    Generates different input distributions.

    Returns:
        Dictionary mapping test names to arrays
    """
    return {
        "Random": [random.randint(0, n) for _ in range(n)],
        "Sorted": list(range(n)),
        "Reverse Sorted": list(range(n, 0, -1)),
        "Repeated Elements": [5] * n
    }


if __name__ == "__main__":
    sizes = [1000, 5000, 10000]

    for size in sizes:
        print(f"\nInput Size: {size}")
        test_cases = generate_test_cases(size)

        for name, data in test_cases.items():

            # Measure deterministic quicksort safely
            try:
                det_time = benchmark(deterministic_quicksort, data)
                det_result = f"{det_time:.5f}s"
            except RecursionError:
                det_result = "RecursionError"

            # Measure randomized quicksort
            rand_time = benchmark(randomized_quicksort, data)

            print(f"{name:20s} | Deterministic: {det_result:15s} | Randomized: {rand_time:.5f}s")
