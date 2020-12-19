import math

students = int(input())
seasons = int(input())

next = 0
new_ones = 0
counter = 1
for i in range(1,seasons+1):
    students = math.ceil(students * 90 / 100)
    counter += 1
    if counter == 2:
        students = math.ceil(students * 90 / 100)
    students = math.ceil(students*80/100)
    if i % 3 == 0:
        students += math.ceil(students * 15 / 100)
    else:
        students += math.ceil(students * 5 / 100)
    counter = 1
print(f'Students: {students}')
