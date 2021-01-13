nums = input().split()

reversed_stack = []

# for _ in range(len(nums)):
#     reverse_nums = nums.pop()
#     reversed_stack.append(reverse_nums)

while nums:
    reversed_stack.append(nums.pop())

print(" ".join(reversed_stack))

# print(*reversed_stack) #work as well as the one above
