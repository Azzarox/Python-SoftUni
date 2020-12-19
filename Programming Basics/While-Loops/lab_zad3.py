num = int(input())
total = 0

while True:
    next_number = int(input())
    total += next_number
    if total >= num:
    #   print(total)
        break

print(total)