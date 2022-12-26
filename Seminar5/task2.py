# 

# numbers = open('file.txt', 'r')
# print(type(numbers.read()))
# print(type(numbers))
#
# numbers_list = numbers.read().split(' ')
# print(numbers_list)

with open('file.txt', 'r') as f:
    nums = list(map(int,f.read().split()))
    print(nums)

for i in range (1, len(nums)):
    if (nums[i] - nums[i - 1]) > 1:
        nums.insert(i, nums[i - 1] + 1 )

print(nums)

data = open('file.txt', 'w')
data.write(' '.join(list(map(str,nums))))
data.close()


