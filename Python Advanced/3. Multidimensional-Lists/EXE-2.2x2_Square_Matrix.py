def read_matrix(is_test=False):
    if is_test:
        return [
            ['A', 'B', 'B', 'D'],
            ['E', 'B', 'B', 'B'],
            ['I', 'J', 'B', 'B'],
        ]
    else:
        row_counts, col_counts = map(int, input().split())
        matrix = []
        for row_index in range(row_counts):
            row = [el for el in input().split()]
            matrix.append(row)
        return matrix


def submatrix(matrix, row, col):
    size = 2
    list_all_items_equal = []
    for r in range(row, row + size):
        for c in range(col, col + size):
            list_all_items_equal.append(matrix[r][c])

    return list_all_items_equal


def check_if_equal(list_i):
    conditions = [list_i[0] == list_i[1] == list_i[2] == list_i[3]]     # слагаме условия, които да се постигнат
    if all(conditions):                                                 # и ги достъпваме с all()
        return True
    return False


def main(matrix):
    counter = 0
    for row in range(len(matrix) - 1):
        for col in range(len(matrix[0]) - 1):
            check_items = submatrix(matrix, row, col)  # вика функцията и проверява 2х2 матрицата на индекс row,col от тази функция
            item = check_if_equal(check_items)         # и записва лист от 4 елемента, фика функцията да провери дали всички елементи са еднакви
            if item:
                counter += 1
    if counter > 0:
        return counter
    return 0


matrix = read_matrix()
res = main(matrix)
print(res)