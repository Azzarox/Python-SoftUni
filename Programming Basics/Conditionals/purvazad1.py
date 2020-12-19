time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes_total = total_time // 60
seconds_total = total_time % 60

if seconds_total < 10:
    print(f'{minutes_total}:0{seconds_total}')
else:
    print(f'{minutes_total}:{seconds_total}')



# zadachata e vqrna i taka s float input

# time_first = float(input()) s float input
# time_second = float(input())
# time_third = float(input())
#
# total_time = time_first + time_second + time_third
#
# minutes_total = total_time // 60
# seconds_total = total_time % 60
#
# if seconds_total < 10:
#     print(f'{minutes_total:.0f}:0{seconds_total:.0f}') :.0f
# else:
#     print(f'{minutes_total:.0f}:{seconds_total:.0f}') :.0f

