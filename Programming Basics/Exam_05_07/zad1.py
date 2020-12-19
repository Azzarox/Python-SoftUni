import math

students = int(input())
tasks = int(input())

total_solutions = students*(math.ceil(tasks * 2.8))
every_third = students * (tasks//3)
total = (total_solutions + every_third)

total_memory = math.ceil(total / 10)
new = total_memory * 5
print(f'{new} KB needed')
print(f'{total} submissions')