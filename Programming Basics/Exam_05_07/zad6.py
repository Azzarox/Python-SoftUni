import math

flag = True
line = input()
while line != "Midnight":
    total_points = 0
    grade = 0
    for i in range(1, 7):
        points = int(input())
        total_points += points
        calculated = math.floor(total_points / 600 * 100)
        grade = calculated * 0.06
        if points < 0:
            print(f'{line} was cheating!')
            flag = False
            grade = 0
            break

    if grade < 3:
        grade = 2.00

    if grade < 5 and flag:
        print(f'{line} - {grade:.2f}')

    elif grade >= 5:
        print(f"""===================
|   CERTIFICATE   |
|    {grade:.2f}/6.00    |
===================
Issued to {line}
    """)
    line = input()

# if grade >= 5.00:
#             print(f""""==================="
# "|   CERTIFICATE   |"
# "|    {grade}/6.00    |"
# "==================="
# "Issued to {line}"
# """)
# else:
#     print(f'{line} - {grade}')
