# ввести дробь, вывести первую цифру дробной части

a = float(input("Введите число "))

d = a % 1
f = d*10
r = f//1

print(int(r))

print(int((a%1)*10))


a = input("Введите число ")  #для строки

for i in range(len(a)):
    if a[i] == ".":
        print(a[i+1])
        break


