def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


def average(values):
    return sum(values) / len(values)


n = int(input())
students_grades_lines = input_to_list(n)

students = {}

for line in students_grades_lines:
    student, grade = line.split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for (student, grades) in students.items():
    avg_grade = average(grades)
    grades_strings = " ".join(map(lambda grade: f'{grade:.2f}', grades))

    # print(f"{student} -> {' '.join(f'{grade:.2f}' for grade in grades)} (avg: {avg_grade:.2f})")
    print(f"{student} -> {grades_strings} (avg: {avg_grade:.2f})")
