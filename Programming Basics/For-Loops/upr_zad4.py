n = int(input())

numbers_200 = 0
numbers_399 = 0
numbers_599 = 0
numbers_799 = 0
numbers_800 = 0
percent1 = 0
percent2 = 0
percent3 = 0
percent4 = 0
percent5 = 0
for i in range(1, n+1):
    number = int(input())
    if number < 200:
        numbers_200 += 1
        percent1 = numbers_200 / n * 100
    elif 200 <= number <= 399:
        numbers_399 += 1
        percent2 = numbers_399 / n * 100
    elif 400 <= number <= 599:
        numbers_599 += 1
        percent3 = numbers_599 / n * 100
    elif 600 <= number <= 799:
        numbers_799 += 1
        percent4 = numbers_799 / n * 100
    elif number >= 800:
        numbers_800 += 1
        percent5 = numbers_800 / n * 100

print(f'{percent1:.2f}%')  #print(f'{numbers_200/n*100:.2f}')
print(f'{percent2:.2f}%')
print(f'{percent3:.2f}%')
print(f'{percent4:.2f}%')
print(f'{percent5:.2f}%')



