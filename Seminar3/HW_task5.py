# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


k = int(input('Введите число: '))

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

def reverse_fib(n):
    return (-1) ** (n + 1) * fib(n)

fib_list = []
for i in range (k + 1):
    fib_list.append(reverse_fib(i))

fib_list.reverse()
fib_list.pop(-1)

for i in range (k + 1):
    fib_list.append(fib(i))
print(fib_list)
