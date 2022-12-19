# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

dec_num = int(input('Введите число: '))
print(dec_num, end = " -> ")
bin_num = ''
while dec_num > 0:
    bin_num = f'{dec_num % 2}{bin_num}'
    dec_num = dec_num // 2
print(bin_num)
