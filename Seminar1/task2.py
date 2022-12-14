# Найти максимальное из 5 чисел
lst = [5, 12, 33, 1, 8]
max = lst[0]

for i in range(1, len(lst)):
    if lst[i] > max:
        max = lst[i]
print(max)
