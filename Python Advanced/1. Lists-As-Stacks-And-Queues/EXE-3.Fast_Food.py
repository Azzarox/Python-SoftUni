# 80/100

from collections import deque

food_quantity = int(input())

queue = deque()

command = input().split(" ")
for el in command:
    queue.append(int(el))

print(max(queue))

while queue:
    order = queue.popleft()
    if order <= food_quantity:
        food_quantity -= order
    elif order > food_quantity:
        queue.append(order)
        print(f'Orders left: {" ".join(list(map(str, queue)))}')
        break

if not queue:
    print("Orders complete")