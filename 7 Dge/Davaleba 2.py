import random
nums = [random.randint(0, 1000) for _ in range(100)]

smallest = nums[0]
largest  = nums[0]

for num in nums:
    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num

print(smallest, largest)