# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*

# *Доп задание: значения коэффициентов от -100 до 100
# *Доп задание: для разного размера уравнения

import random


k = int(input("Введите число k : "))
coef1 = [random.randint(1,100) for i in range(0, k + 1)]
coef2 = [random.randint(1,100) for i in range(0, k + 1)]
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



str_num_1 = ""
str_num_2 = ""

with open('pol1.txt', 'r') as file:
    for line in file:
        str_num_1 = line

with open('pol2.txt', 'r') as file:
    for line in file:
        str_num_2 = line


dict_1 = {}
dict_2 = {}

str_num_1 = str_num_1.split(" = ")[0]
str_num_2 = str_num_2.split(" = ")[0]
str_num_1_list = str_num_1.split(" + ")
str_num_2_list = str_num_2.split(" + ")

for i in range(len(str_num_1_list)):
    if str_num_1_list[i].count("x^"):
        dict_1[int(str_num_1_list[i].split("^")[1])] = int(str_num_1_list[i].split("*")[0])
    elif str_num_1_list[i].count("x"):
        dict_1[1] = int(str_num_1_list[i].split("*")[0])
    else:
        dict_1[0] = int(str_num_1_list[i])
print(dict_1)

for i in range(len(str_num_2_list)):
    if str_num_2_list[i].count("x^"):
        dict_2[int(str_num_2_list[i].split("^")[1])] = int(str_num_2_list[i].split("*")[0])
    elif str_num_2_list[i].count("x"):
        dict_2[1] = int(str_num_2_list[i].split("*")[0])
    else:
        dict_2[0] = int(str_num_2_list[i])
print(dict_2)

max_index = 0
for key in dict_1.keys():
    if max_index < key:
        max_index = key
for key in dict_2.keys():
    if max_index < key:
        max_index = key

dict_3 = {}
for i in range(max_index, -1, - 1):
    if i in dict_1:
        if i in dict_2:
            dict_3[i] = dict_1[i] + dict_2[i]
        else:
            dict_3[i] = dict_1[i]
    elif i in dict_2:
        dict_3[i] = dict_2[i]
print(dict_3)

final_list = []
for i in range(max_index, -1, - 1):
    if i in dict_3:
        if i == 1:
            final_list.append(str(dict_3[i]) + "*x")
        elif i == 0:
            final_list.append(str(dict_3[i]))
        else:
            final_list.append(str(dict_3[i]) + "*x^" + str(i))

with open('pol3.txt', 'w') as file:
    print(*final_list, file=file, sep=' + ', end=' = 0\n')
