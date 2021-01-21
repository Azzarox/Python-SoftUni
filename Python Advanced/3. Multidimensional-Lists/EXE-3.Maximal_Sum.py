# my code

def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 5, 5, 2, 4],
            [2, 1, 4, 14, 3],
            [3, 7, 11, 2, 8],
            [4, 8, 12, 16, 4],
        ]
    else:
        rows_count, col_count = map(int, input().split())
        matrix = []
        for row_index in range(rows_count):
            row = [int(el) for el in input().split()]
            matrix.append(row)
        return matrix


def submatrix_3x3(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]
    return the_sum


def main(matrix, size):
    best_row_index = 0
    best_col_index = 0
    best_sum = submatrix_3x3(matrix, 0, 0, size)
    for row_index in range(len(matrix) - size + 1):
        for col_index in range(len(matrix[0]) - size + 1):
            current_sum = submatrix_3x3(matrix, row_index, col_index, size)
            if current_sum > best_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_col_index = col_index
    return best_row_index, best_col_index, best_sum


def print_result(coordinates, size):
    rows_index, cols_index, best_sum = coordinates
    print(f'Sum = {best_sum}')
    for r in range(rows_index, rows_index + size):
        row = []
        for c in range(cols_index, cols_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))


matrix = read_matrix()
SIZE = 3
coordinates = main(matrix, SIZE)
print_result(coordinates, SIZE)
