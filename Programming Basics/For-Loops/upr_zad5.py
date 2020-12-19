n = int(input())

numbers_2 = 0
numbers_3 = 0
numbers_4 = 0
for i in range(1,n+1):
    number = int(input())
    if number % 2 == 0:
        numbers_2 += 1
    if number % 3 ==0:
        numbers_3 += 1
    if number % 4 == 0:
        numbers_4 += 1

print(f'{numbers_2/n*100:.2f}%')
print(f'{numbers_3/n*100:.2f}%')
print(f'{numbers_4/n*100:.2f}%')