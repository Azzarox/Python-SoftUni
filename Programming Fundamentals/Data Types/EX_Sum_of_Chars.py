n = int(input())

total = 0
for i in range(n):
    new = input()
    ascii_char = ord(new)
    total += ascii_char

print(f'The sum equals: {total}')