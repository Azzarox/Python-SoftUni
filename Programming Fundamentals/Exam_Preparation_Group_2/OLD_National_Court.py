first_e = int(input())
second_e = int(input())
third_e = int(input())
total_people_count = int(input())

people_per_hour = sum([first_e, second_e, third_e])

hours = 0

while total_people_count > 0:
    total_people_count -= people_per_hour
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f'Time needed: {hours}h.')
