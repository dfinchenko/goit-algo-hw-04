import timeit
import random

# Функції сортування
def sort_merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        sort_merge(left)
        sort_merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def sort_insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def timsort(arr):
    arr.sort()

# Замір часу виконання для кожного алгоритму на кожному масиві
time_results = {}
sizes = [100, 500, 1000]

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]
    time_results[size] = {
        'Merge sort': min(timeit.repeat(lambda: sort_merge(arr.copy()), number=1, repeat=5)),
        'Insertion sort': min(timeit.repeat(lambda: sort_insertion(arr.copy()), number=1, repeat=5)),
        'Timsort': min(timeit.repeat(lambda: timsort(arr.copy()), number=1, repeat=5))
    }

# Результат
for size, timings in time_results.items():
    print(f"Розмір масиву: {size} елементів")
    for sort_method, time in timings.items():
        print(f"  {sort_method}: {time:.6f} секунди")