from collections import deque

supermarket_queue = deque()

while True:

    command = input()

    if command == "Paid":
        while supermarket_queue:
            print(supermarket_queue.popleft())

    elif command == "End":
        print(f"{len(supermarket_queue)} people remaining.")
        break
    else:
        name = command
        supermarket_queue.append(name)
