from typing import List

lst1 = [68.559, 34.1, 64.56, 47.0, 68.568, 98.48, 33.74, 16.899,
        43.643, 77.62, 24.12, 82.4, 88.487, 15.22, 2.6]

# sorted   [2.6, 15.22, 16.899, 24.12, 33.74, 34.1, 43.643, 47.0, 64.56, 68.559, 68.568, 77.62,
# 82.4, 88.487, 98.48]


def binary_search(lst: List[float], target: float):

    arr = lst.copy()
    arr.sort()

    if target < arr[0] or target > arr[-1]:
        return f"Number {target} is out of set"

    low = 0
    high = len(arr) - 1

    count = 0
    res = high
    while low <= high:
        count += 1

        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            res = mid
            high = mid - 1

        else:
            res = mid
            break

    return (count, arr[res])


print("Sorted list", sorted(a for a in lst1))
print("34.1 -> ", binary_search(lst1, 34.1))
print("64.56 -> ", binary_search(lst1, 64.56))
print("24.12 -> ", binary_search(lst1, 24.12))
print("24.01 -> ", binary_search(lst1, 24.01))
print("1.2 -> ", binary_search(lst1, 1.2))
print("99.1 -> ", binary_search(lst1, 99.1))
