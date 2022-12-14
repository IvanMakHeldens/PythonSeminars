# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой


str1 = input('Введите первую строчку')
str2 = input('Введите вторую строчку')

str1_arr = str1.split(' ')
count = 0
for i in str1_arr:
    if i in str2:
        count += 1
print(count)

print(str1.lower().count(str2.lower()))
