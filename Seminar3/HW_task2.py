# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

nums = [2, 3, 4, 5, 6]

def nums_pair_prod(nums):
    prod = []
    half_len = len(nums) // 2
    for i in range(0, half_len):
        prod.append(nums[i] * nums[-i -1])
    if len(nums) % 2 != 0:
        prod.append(nums[half_len] ** 2)
    print(nums, end =' => ')
    return prod

print(nums_pair_prod(nums))
print(nums_pair_prod(nums = [2, 3, 5, 6]))