def func(arr):
    total = 0
    n = len(arr)
    original_arr = arr.copy()
    for i in range(n):
        if (i > 0 and original_arr[i - 1] == 10) or ( i > 1 and original_arr[i - 2] == 10):
            arr[i] *= 2
        total += arr[i]
    return total


arrays = [
    [1, 2, 3],
    [8, 10, 10, 2],
    [8, 10, 4, 5, 3]
]
max_sum = 0
largest_array = None
for arr in arrays:
    current_sum = func(arr)
    print(current_sum)
    if current_sum > max_sum:
        max_sum = current_sum
        largest_array = arr
print('Масив з найбільшою сумою:', largest_array, 'Сума: ', max_sum)









