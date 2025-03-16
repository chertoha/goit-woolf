import random
import time
import numpy as np
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Використовуємо середній елемент як опорний
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_func, arr, runs=5):
    times = []
    for _ in range(runs):
        arr_copy = arr.copy()
        start = time.time()
        sort_func(arr_copy)
        end = time.time()
        times.append(end - start)
    return np.mean(times)

sizes = [10_000, 50_000, 100_000, 500_000]
rand_times, det_times = [], []

for size in sizes:
    test_array = [random.randint(0, 10**6) for _ in range(size)]
    rand_times.append(measure_time(randomized_quick_sort, test_array))
    det_times.append(measure_time(deterministic_quick_sort, test_array))
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {rand_times[-1]:.4f} секунд")
    print(f"   Детермінований QuickSort: {det_times[-1]:.4f} секунд")

plt.plot(sizes, rand_times, label="Рандомізований QuickSort")
plt.plot(sizes, det_times, label="Детермінований QuickSort", linestyle='dashed')
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.legend()
plt.show()
