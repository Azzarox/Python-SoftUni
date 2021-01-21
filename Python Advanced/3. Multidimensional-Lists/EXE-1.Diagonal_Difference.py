def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    else:
        rows_count = int(input())
        matrix = []
        for row_index in range(rows_count):
            row = [int(el) for el in input().split()]
            matrix.append(row)
        return matrix


def primary_d(matrix, size):
    sum_primary_diagonal = 0
    for row_index in range(size):
        sum_primary_diagonal += matrix[row_index][row_index]
    return sum_primary_diagonal


def secondary_d(matrix, size):
    sum_secondary_diagonal = 0
    for row_index in range(size):
        sum_secondary_diagonal += matrix[row_index][size - row_index - 1]
    return sum_secondary_diagonal


matrix = read_matrix()
size = len(matrix)
abs_value = abs(primary_d(matrix, size) - secondary_d(matrix, size))
print(abs_value)
