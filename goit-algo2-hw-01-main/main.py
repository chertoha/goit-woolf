arr = [92, 25, 35, 97, 95, 56, 90, 60, 32, 94, 60, 50, 37, 9, 22]


def min_max(arr):
    if len(arr) == 1:
        return (arr[0], arr[0])

    if len(arr) == 2:
        return (min(arr), max(arr))

    mid = len(arr) // 2
    left_min, left_max = min_max(arr[:mid])
    right_min, right_max = min_max(arr[mid:])

    return (min(left_min, right_min), max(left_max, right_max))


print(min_max(arr))
