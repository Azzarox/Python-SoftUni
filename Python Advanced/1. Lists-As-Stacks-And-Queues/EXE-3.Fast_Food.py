# 100/100

from collections import deque

food_quantity = int(input())

queue = deque(map(int, input().split(" ")))
print(max(queue))

while queue:
    order = queue[0]  # става като peek, без да pop-ваме
    if order <= food_quantity:
        order = queue.popleft()
        food_quantity -= order

    elif order > food_quantity:
        break

if not queue:
    print("Orders complete")
else:
    print(f'Orders left: {" ".join(list(map(str, queue)))}')