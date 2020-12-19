n = int(input())

capacity = 255

total = 0
for i in range(n):
    litre = int(input())
    total += litre
    if total > capacity:
        print('Insufficient capacity!')
        total -= litre
print(total)

# while loop #
# n = int(input())
# capacity = 255
#
# counter = 0
# total = 0
# while True:
#     if counter == n:
#         break
#     else:
#         litre = int(input())
#         counter += 1
#         total += litre
#         if total > capacity:
#             print('Insufficient capacity!')
#             total -= litre
# print(total)



# another approach
# n = int(input())
#
# capacity = 255
#
# for i in range(n):
#     litre = int(input())
#     if capacity - litre < 0:
#         print('Insufficient capacity!')
#     else:
#         capacity -= litre
#
# print(255-capacity)