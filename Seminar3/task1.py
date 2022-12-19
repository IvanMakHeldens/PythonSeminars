# реализуйте алгоритм перемешивания списка
import time
import random


def rand_num(min = 0, max = 10):
    num = int((time.time() %1 ) * (max - min) + min)
    return num


lst = [2, -10, 5, 8, 43]
# random.shuffle(lst)
# print(lst)
print(lst)
for i in range(len(lst)):
    j = rand_num(0, len(lst) - 1)
    temp = lst[i]
    lst[i], lst[j] = lst[j], lst[i]
print(lst)
for i in range(len(lst)):
    j = rand_num(0, len(lst) - 1)
    temp = lst[i]
    lst[i], lst[j] = lst[j], lst[i]
print(lst)
for i in range(len(lst)):
    j = rand_num(0, len(lst) - 1)
    temp = lst[i]
    lst[i], lst[j] = lst[j], lst[i]
print(lst)
for i in range(len(lst)):
    j = rand_num(0, len(lst) - 1)
    temp = lst[i]
    lst[i], lst[j] = lst[j], lst[i]
print(lst)