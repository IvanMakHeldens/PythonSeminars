# Ввести N, вывести числа от -N до N

N = int(input("введите N "))

nums = []
for i in range(-abs(N), abs(N)+1):
    nums.append(i)
print(nums)

for i in range(-abs(N), abs(N)+1):
    print(i, end="  ")




