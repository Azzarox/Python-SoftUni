data = input()

course_book_students = {}

while not data == "end":

    course_name, student_name = data.split(" : ")

    if course_name not in course_book_students:
        course_book_students[course_name] = []
        course_book_students[course_name] = [student_name]
    else:
        course_book_students[course_name].append(student_name)

    data = input()

# order = sorted(info.items(), key=lambda x: (-len(x[1]), x[0]))
order = sorted(course_book_students.items(), key=lambda x: len(x[1]), reverse=True)

for key, value in order:
    print(f'{key}: {len(value)}')
    for student_name in sorted(value):
        print(f'-- {student_name}')
