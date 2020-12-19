task = int(input())
points = int(input())
course = input()

coef = 0
if course == "Basics":
    if task == 1:
        coef = 8
    elif task == 2:
        coef = 9
    elif task == 3:
        coef = 9
    elif task == 4:
        coef = 10
elif course == "Fundamentals":
    if task == 1:
        coef = 11
    elif task == 2:
        coef = 11
    elif task == 3:
        coef = 12
    elif task == 4:
        coef = 13
elif course == "Advanced":
    if task == 1:
        coef = 14
    elif task == 2:
        coef = 14
    elif task == 3:
        coef = 15
    elif task == 4:
        coef = 16

total = points * (coef / 100)
if course == "Advanced":
    total += total * 0.2
elif course == "Basics" and task == 1:
    total -= total *0.2

print(f'Total points: {total:.2f}')
