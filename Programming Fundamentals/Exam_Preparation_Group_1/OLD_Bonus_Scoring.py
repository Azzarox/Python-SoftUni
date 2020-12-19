import math

students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())

max_number = 0
max_bonus_attendances = 0
for i in range(students_count):
    attendance_count = int(input())

    total_bonus = attendance_count / lectures_count * (5 + initial_bonus)

    if total_bonus > max_number:
        max_number = total_bonus
        max_bonus_attendances = attendance_count


print(f'Max Bonus: {math.ceil(max_number)}.')
print(f'The student has attended {max_bonus_attendances} lectures.')
