n = int(input())

sum_left = 0
sum_right = 0

for i in range(n):            #trqbva da e do n(input) a ne do "2" kakto go bqh slojil
    number = int(input())
    sum_left += number

for i in range(n):
    num = int(input())
    sum_right += num

if sum_right == sum_left:
    print(f'Yes, sum = {sum_right}')
else:
    print(f'No, diff = {abs(sum_right - sum_left)}')