# Задача: предложить улучшения кода(3-5задач) для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


my_list = list(map(int, input('Введите числа, через пробел: ').split()))
print(sum(my_list[1::2]))