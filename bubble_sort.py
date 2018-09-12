def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


my_data = [5, 2, 9, 34, 6, 1, 7]

bubble_sort(my_data)

print(my_data)
