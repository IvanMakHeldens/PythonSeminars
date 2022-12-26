# посчитать нок и нод

n1 = int(input("Введите целое число: "))
n2 = int(input("Введите целое число: "))

list_of_factor = []
list_of_factor_2 = []

def f(n, list):
    num_factor = 2
    while n > 1:
        if n % num_factor == 0:
            list.append(num_factor)
            n = int(n / num_factor)
        else:
            num_factor += 1

f(n1, list_of_factor)
f(n2, list_of_factor_2)
print(set(list_of_factor))
print(set(list_of_factor_2))

print(set(list_of_factor).intersection(set(list_of_factor_2)))
nod_find = set(list_of_factor).intersection(set(list_of_factor_2))

nod = 1
for i in nod_find:
    nod = nod * i

nok = n1 * n2 / nod
print(nok)
print(nod)


# final_list = []
# for i in list_of_factor:
#     for j in list_of_factor_2:
#         if i in 
