numbers = input().split(', ')
beggars = int(input())
sums = [0] * beggars

while numbers:
    for beggar in range(beggars):
        if not numbers:
            break

        sums[beggar] += int(numbers.pop(0))

print(sums)



# nums = input()
# beggars = int(input())
# nums_list = nums.split(', ')
# profit = []
# for i in range(beggars):
#     profit.append(0)
# i = 0
# while len(nums_list)>0:
#     nums_list[0] = int(nums_list[0])
#     if i < len(profit):
#         profit[i]+=nums_list[0]
#     else:
#         i = 0
#         continue
#     nums_list.pop(0)
#     i+=1
# print(profit)



# some shit ???

# numbers_list = input().split(', ')
# number_of_beggars = int(input())
# beggars_turn = number_of_beggars
# int_list = []
# count_list = []
# counter = 0
#
# for element in numbers_list:
#     int_list.append(int(element))
#
# for zero in range(number_of_beggars):
#     count_list.append(0)
#
# for zero_2 in range(number_of_beggars):
#     count_list[zero_2] += int_list[zero_2]
#
# print(count_list)
