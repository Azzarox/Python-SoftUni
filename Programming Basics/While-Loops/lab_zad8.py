name = input()
total = 0
classes = 0

while True:
    grade = float(input())
    classes += 1
    total = total + grade

    if grade < 4.00:
        print(f'{name} has been excluded at {classes} grade')
        break

    if classes == 12:
        print(f"{name} graduated. Average grade: {total / 12:.2f}")
        break
