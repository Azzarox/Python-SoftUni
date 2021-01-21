# my code and from presentation help


# make matrix

rows, columns = map(int, input().split())
text = input()

matrix = []
for r in range(rows):
    matrix.append([0] * columns)


# fill the matrix with

index = 0
for row_index in range(rows):
    for col_index in range(columns):
        # noinspection PyTypeChecker
        # изключва TypeChecker-а, на col_index отдолу
        matrix[row_index][col_index] = text[index]
        index += 1
        if index == len(text):
            index = 0


# print the matrix

for row_index in range(rows):
    if row_index % 2 != 0:
        # print(f''.join(matrix[row_index][::-1])) # За да работи трябва да сложим долният принт в else-а
        matrix[row_index].reverse()
    print("".join(matrix[row_index]))
