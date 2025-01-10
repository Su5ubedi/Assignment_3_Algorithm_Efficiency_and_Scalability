import random
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(1500)

# Randomize Quicksort Implementation
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Deterministic Quicksort Implementation
def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)

# Helper Function for Timing Algorithms
def time_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr, 0, len(arr) - 1)
    return time.time() - start_time

# Generate Arrays for Testing
def generate_test_arrays():
    sizes = [10, 50, 100, 500, 1000]
    test_cases = {
        "Random": [random.sample(range(10**6), size) for size in sizes],
        "Sorted": [list(range(size)) for size in sizes],
        "Reverse-Sorted": [list(range(size, 0, -1)) for size in sizes],
        "Repeated-Elements": [[random.randint(1, 10) for _ in range(size)] for size in sizes],
    }
    return sizes, test_cases

# Main Function
def main():
    sizes, test_cases = generate_test_arrays()
    results = []

    for case, arrays in test_cases.items():
        print(f"\nAnalyzing {case} arrays...")
        for arr in arrays:
            print(f"  Testing array of size {len(arr)}...")
            random_arr = arr[:]
            det_arr = arr[:]

            try:
                randomized_time = time_algorithm(randomized_quicksort, random_arr)
                deterministic_time = time_algorithm(deterministic_quicksort, det_arr)
            except RecursionError:
                print(f"  Recursion error for array of size {len(arr)}.")
                continue
            except Exception as e:
                print(f"  Error for array of size {len(arr)}: {e}")
                continue

            results.append((case, len(arr), randomized_time, deterministic_time))
            print(f"    Randomized: {randomized_time:.4f}s, Deterministic: {deterministic_time:.4f}s")

    # Print Results
    print("\nPerformance Results:")
    for result in results:
        case, size, randomized, deterministic = result
        print(f"{case} Array | Size: {size} | Randomized: {randomized:.4f}s | Deterministic: {deterministic:.4f}s")

    # Plot Results
    for case in test_cases.keys():
        case_results = [r for r in results if r[0] == case]
        sizes = [r[1] for r in case_results]
        rand_times = [r[2] for r in case_results]
        det_times = [r[3] for r in case_results]

        plt.figure()
        plt.plot(sizes, rand_times, label="Randomized Quicksort", marker="o")
        plt.plot(sizes, det_times, label="Deterministic Quicksort", marker="o")
        plt.title(f"Performance Comparison: {case} Arrays")
        plt.xlabel("Array Size")
        plt.ylabel("Time (s)")
        plt.legend()
        plt.xscale("log")
        plt.yscale("log")
        plt.grid()
        plt.show()

if __name__ == "__main__":
    main()
