groups_count = int(input())

total = 0
group_1,group_2,group_3,group_4,group_5 = 0,0,0,0,0

for i in range(groups_count):
    people_in_group = int(input())
    total += people_in_group
    if people_in_group <= 5:
        group_1 += people_in_group
    elif people_in_group <= 12:
        group_2 += people_in_group
    elif people_in_group <= 25:
        group_3 += people_in_group
    elif people_in_group <= 40:
        group_4 += people_in_group
    elif people_in_group >= 41:
        group_5 += people_in_group


print(f'{group_1/total*100:.2f}%')
print(f'{group_2/total*100:.2f}%')
print(f'{group_3/total*100:.2f}%')
print(f'{group_4/total*100:.2f}%')
print(f'{group_5/total*100:.2f}%')
