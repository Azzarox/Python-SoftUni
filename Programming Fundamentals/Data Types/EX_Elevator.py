import math
people = int(input())
capacity = int(input())

x = math.ceil(people/capacity)
print(x)


#same but with different approach

# people = int(input())
# capacity = int(input())
#
# if not people % capacity == 0:
#     x = people // capacity + 1
# else:
#     x = people // capacity
# print(x)