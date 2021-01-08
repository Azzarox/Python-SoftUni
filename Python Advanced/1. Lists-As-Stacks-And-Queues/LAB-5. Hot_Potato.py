# my_code = 100/100

from collections import deque

kids = deque(input().split())
n_toss = int(input())

while len(kids) > 1:
    for i in range(1, n_toss + 1):
        if i != n_toss:
            kid_to_be_rotated = kids.popleft()
            kids.append(kid_to_be_rotated) # the same as kids.append(kids.popleft())
        else:
            kid_to_be_removed = kids.popleft()
            print(f'Removed {kid_to_be_removed}')

print(f'Last is {"".join(kids)}')


# with Rotate

# from collections import deque
#
# kids = deque(input().split())
# n_toss = int(input())
#
# while kids:
#     kids.rotate(
#         -n_toss + 1)  # -n_toss + 1 , защото трябва да завърти 1 елемент по-малко (защото брои от 0 (0,1) - (1, 2) )
#     kid_pop = kids.popleft()
#
#     if kids:
#         print(f'Removed {kid_pop}')
#     else:
#         print(f'Last is {kid_pop}')


# with counter/index - почти като моя код

# from collections import deque
#
# kids = deque(input().split())
# n_toss = int(input())
# counter = 0
#
# while kids:
#     counter += 1
#     kid_pop = kids.popleft()
#     if counter == n_toss:
#         if kids:
#             counter = 0
#             print(f'Removed {kid_pop}')
#         else:
#             print(f'Last is {kid_pop}')
#     else:
#         kids.append(kid_pop)
