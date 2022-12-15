# Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.(Не используя библиотеки связанные с рандомом)

import time

start = int(input('Нижний предел: '))
end = int(input('Верхний предел: '))
rand_num = int(round((time.time()%1)*(end-start) + start, 0))
print(f'Случайное число в диапазоне от {start} до {end} : {rand_num}')