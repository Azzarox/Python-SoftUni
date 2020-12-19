n = int(input())

student_book = {}

for _ in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in student_book:
        student_book[student_name] = []
    student_book[student_name].append(grade)

students_with_average_result = {}

for key, value in student_book.items():
    average = sum(value) / len(value)
    if average >= 4.50:
        students_with_average_result[key] = average

order_students = sorted(students_with_average_result.items(), key=lambda x: -x[1])

for key,value in order_students:
    print(f'{key} -> {value:.2f}')

