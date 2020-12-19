n = int(input())

even_sum = 0
odd_sum = 0

for i in range(n):
    new_number = int(input())
    if i % 2 == 0:
        even_sum += new_number
    else:
        odd_sum += new_number

if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    print(f'Diff = {abs(even_sum - odd_sum)}')

# n = int(input())
#
# even_sum = 0
# odd_sum = 0
#
# if n % 2 == 0:
#     for i in range(n - 2):
#         odd_number = int(input())
#         odd_sum += odd_number
#         even_number = int(input())
#         even_sum += even_number
#
# else:
#     for i in range(n+1):
#         odd_number = int(input())
#         odd_sum += odd_number
#         even_number = int(input())
#         even_sum += even_number
#
# if odd_sum == even_sum:
#     print('Yes')
#     print(f'Sum = {even_sum}')
# else:
#     print('No')
#     print(f'Diff = {abs(even_sum - odd_sum)}')


# works only if n is even number


