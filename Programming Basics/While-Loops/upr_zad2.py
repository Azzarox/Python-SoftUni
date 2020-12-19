# bad_grades = int(input())   # za da prekratim cikula ako se stigne do nomera na bad_grades
# total = 0                   # za da izchislim average
# total_grades_count = 0      # za da izchislim average
# bad_grades_count = 0

bad_grades = int(input())
bad_grades_count = 0
grades = 0
total = 0
last  = ''

while True:
    name = input()

    if name == "Enough":                           # slagame grade int input sled if construkciqta
        print(f'Average score: {total / grades:.2f}')  # zashtoto inache sravnqva int s Enough
        print(f'Number of problems: {grades}')     # i guess
        print(f'Last problem: {last}')
        break

    last = name      # slagame tuka zashtot ako e nad if-a shte pazi kato posledno "Enough"

    grade = int(input())
    total += grade
    grades += 1

    if grade <= 4.00:
        bad_grades_count += 1

    if bad_grades == bad_grades_count:
        print(f"You need a break, {bad_grades_count} poor grades.")
        break

# --------------------------
# -    working upper^      -
# --------------------------
# -  working down as well  -
# --------------------------

# bad_grades = int(input())
# bad_grades_count = 0
# total_grades_count = 0
# grades_sum = 0
# last_name = ''
#
# while True:
#     name = input()
#     if name == "Enough":
#         print(f'Average score: {grades_sum / total_grades_count:.2f}')
#         print(f'Number of problems: {total_grades_count}')
#         print(f'Last problem: {last_name}')
#         break
#
#     last_name = name
#     grade = int(input())
#     total_grades_count += 1
#     grades_sum += grade
#
#     if grade <= 4:
#         bad_grades_count += 1
#
#     if bad_grades_count == bad_grades:
#         print(f"You need a break, {bad_grades_count} poor grades.")
#         break