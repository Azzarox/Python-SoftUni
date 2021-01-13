
# 80/100
n = int(input())

stack = []

for _ in range(n):
    data = input().split()
    command = data[0]
    if command == "1":
        number = int(data[1])  # number = int(data[0])
        stack.append(number)
    elif command == "2":
        if len(stack) > 0:
            stack.pop()
    elif command == "3":
        print(max(stack))
    elif command == "4":
        print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(stack.pop())

print(", ".join(list(map(str, reversed_stack))))
