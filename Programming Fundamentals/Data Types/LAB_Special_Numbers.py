n = int(input())

for i in range(1,n+1):
    digits_sum = 0
    for digit in str(i):
        digits_sum += int(digit)
    if digits_sum in [5,7,11]:
        print(f'{i} -> True')
    elif digits_sum not in [5,7,11]:
        print(f'{i} -> False')