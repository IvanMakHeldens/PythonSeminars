# Вычислить число Пи c заданной точностью d
# Пример:
#     - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10


import math


d = int(input('Введите точность округления числа Пи: '))
x = str(math.pi)
print(x[0:d+2:1])