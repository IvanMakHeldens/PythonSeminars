# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число: "))

main_n = n
list_of_factor = []
num_factor = 2
while n > 1:
    if n % num_factor == 0:
        list_of_factor.append(num_factor)
        n = int(n / num_factor)
    else:
        num_factor += 1
    
print(f'{main_n} = ', end = '')
print(*list_of_factor, sep = " * ")