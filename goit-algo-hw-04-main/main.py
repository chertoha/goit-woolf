from merge_sort import merge_sort
from insertion_sort import insertion_sort
from timeit import timeit
import random


def main():
    small_data = [random.randint(0, 1000) for _ in range(100)]
    medium_data = [random.randint(0, 10000) for _ in range(1000)]
    large_data = [random.randint(0, 100000) for _ in range(10000)]

    insertion_small = timeit(lambda: insertion_sort(small_data), number=3)
    merge_small = timeit(lambda: merge_sort(small_data), number=3)
    sorted_timsort_small = timeit(lambda: sorted(small_data), number=3)
    sort_timsort_small = timeit(lambda: small_data[:].sort(), number=3)

    insertion_medium = timeit(lambda: insertion_sort(medium_data), number=3)
    merge_medium = timeit(lambda: merge_sort(medium_data), number=3)
    sorted_timsort_medium = timeit(lambda: sorted(medium_data), number=3)
    sort_timsort_medium = timeit(lambda: medium_data[:].sort(), number=3)

    insertion_large = timeit(lambda: insertion_sort(large_data), number=3)
    merge_large = timeit(lambda: merge_sort(large_data), number=3)
    sorted_timsort_large = timeit(lambda: sorted(large_data), number=3)
    sort_timsort_large = timeit(lambda: large_data[:].sort(), number=3)

    print(f"| {"Alg":<20} | {"Small data":^20} | {
          "Medium data":^20} | {"Large data":^20} |")

    print(f"| {"-"*20} | {"-"*20} | {"-"*20} | {"-"*20} |")

    print(f"| {"Insertion sort":<20} | {insertion_small:^20.5f} | {
          insertion_medium:^20.5f} | {insertion_large:^20.5f} |")

    print(f"| {"Merge sort":<20} | {merge_small:^20.5f} | {
          merge_medium:^20.5f} | {merge_large:^20.5f} |")

    print(f"| {"Timsort (sorted)":<20} | {sorted_timsort_small:^20.5f} | {
          sorted_timsort_medium:^20.5f} | {sorted_timsort_large:^20.5f} |")

    print(f"| {"Timsort (sort)":<20} | {sort_timsort_small:^20.5f} | {
          sort_timsort_medium:^20.5f} | {sort_timsort_large:^20.5f} |")


if __name__ == "__main__":
    main()
