students = int(input())
tasks = int(input())
energy = int(input())

total_tasks =0
total_questions = 0
questions = 0
while True:
    energy += tasks * 2
    students -= tasks
    questions = students * 2
    energy -= questions * 3
    total_tasks += tasks
    total_questions += questions
    if students >= 10:
        students += students//10
    else:
        print(f'The students are too few!')
        print(f'Problems solved: {total_tasks}')
        break
    if energy <= 0:
        print(f'The trainer is too tired!')
        print(f'Questions asked: {total_questions}')
        break

