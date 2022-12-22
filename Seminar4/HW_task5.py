# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*

# *Доп задание: значения коэффициентов от -100 до 100
# *Доп задание: для разного размера уравнения

import random


k = int(input("Введите число k : "))
coef1 = [random.randint(-100,100) for i in range(0, k + 1)]
coef2 = [random.randint(-100,100) for i in range(0, k + 1)]
print(coef1)
print(coef2)
def Polynom(k, coef):
    pol = ''
    for i in range(0, k + 1):
        if k - i > 1 and coef[i] != 0:
            pol += f'{coef[i]}*x^{k - i} + '
        elif k - i == 1 and coef[i] != 0:
            pol += f'{coef[i]}*x + '
        else:
            pol += f'{coef[i]} = 0'
    return pol

with open('pol1.txt', 'w') as data:
    data.write(Polynom(k, coef1).replace('+ -', '- '))
print((Polynom(k, coef1).replace('+ -', '- ')))

with open('pol2.txt', 'w') as data:
    data.write(Polynom(k, coef2).replace('+ -', '- '))
print((Polynom(k, coef2).replace('+ -', '- ')))