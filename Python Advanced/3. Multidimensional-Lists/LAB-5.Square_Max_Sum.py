# my code almost solo ugly af

def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:
        (rows_count, columns_count) = map(int, input().split(", "))
        matrix = []
        for row in range(rows_count):
            rows = [int(el) for el in input().split(", ")]
            matrix.append(rows)
        return matrix


def calc_current_matrix_sum(matrix):
    cur_sum = matrix[row_index][col_index] \
              + matrix[row_index][col_index + 1] \
              + matrix[row_index + 1][col_index] \
              + matrix[row_index + 1][col_index + 1]
    return cur_sum


def print_result(matrix):
    print(
        f'{matrix[best_row_index][best_col_index]} {matrix[best_row_index][best_col_index + 1]}\n{matrix[best_row_index + 1][best_col_index]} {matrix[best_row_index + 1][best_col_index + 1]}')


matrix = read_matrix()

best_sum = 0
best_row_index = 0
best_col_index = 0
for row_index in range(len(matrix) - 2 + 1):
    for col_index in range(len(matrix[0]) - 2 + 1):
        current_sum = calc_current_matrix_sum(matrix)
        if current_sum > best_sum:
            best_col_index = col_index
            best_row_index = row_index
            best_sum = current_sum

print_result(matrix)
print(best_sum)


# TODO: from presentation lab
#
# def read_matrix(is_test=False):
#     if is_test:
#         return [
#             [7, 1, 3, 3, 2, 1],
#             [1, 3, 9, 8, 5, 6],
#             [4, 6, 7, 9, 1, 0],
#         ]
#     else:
#         (rows_count, columns_count) = map(int, input().split(', '))
#         matrix = []
#         for row_index in range(rows_count):
#             row = [int(x) for x in input().split(', ')]
#             matrix.append(row)
#
#         return matrix
#
#
# def get_sum_of_submatrix(matrix, row_index, column_index, size):
#     the_sum = 0
#     for r in range(row_index, row_index + size):
#         for c in range(column_index, column_index + size):
#             the_sum += matrix[r][c]
#     return the_sum
#
#
# def get_best_submatrix_sum_coordinates(matrix, submatrix_size):
#     best_row_index = 0
#     best_column_index = 0
#     best_sum = get_sum_of_submatrix(matrix, 0, 0, submatrix_size)
#
#     for row_index in range(len(matrix) - submatrix_size + 1):
#         for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
#             current_sum = get_sum_of_submatrix(matrix, row_index, col_index, submatrix_size)
#             if best_sum < current_sum:
#                 best_sum = current_sum
#                 best_row_index = row_index
#                 best_column_index = col_index
#     return (best_row_index, best_column_index)
#
#
# def print_result(coordinates, size):
#     (row_index, col_index) = coordinates
#     for r in range(row_index, row_index + size):
#         row = []
#         for c in range(col_index, col_index + size):
#             row.append(matrix[r][c])
#         print(' '.join(str(x) for x in row))
#     print(get_sum_of_submatrix(matrix, row_index, col_index, size))
#
#
# SUBMATRIX_SIZE = 2
#
# matrix = read_matrix(is_test=True)
# coordinates = get_best_submatrix_sum_coordinates(matrix, SUBMATRIX_SIZE)
# print_result(coordinates, SUBMATRIX_SIZE)

# TODO: rewritten from presentation lab
# def read_matrix(is_test=False):
#     if is_test:
#         return [
#             [7, 1, 3, 3, 2, 1],
#             [1, 3, 9, 8, 5, 6],
#             [4, 6, 7, 9, 1, 0],
#         ]
#     else:
#         (rows_counts, cols_count) = map(int, input().split(", "))
#         matrix = []
#         for row_index in range(rows_counts):
#             row = [int(el) for el in input().split(", ")]
#             matrix.append(row)
#         return matrix
#
#
# def sum_of_submatrix_2x2(matrix, row_index, col_index, size):
#     the_sum = 0
#     for row in range(row_index, row_index + size):
#         for col in range(col_index, col_index + size):
#             the_sum += matrix[row][col]
#     return the_sum
#
#
# def iterate_over_real_matrix(matrix, submatrix_size):
#     best_row_index = 0
#     best_col_index = 0
#     best_sum = sum_of_submatrix_2x2(matrix, 0, 0, submatrix_size)
#
#     for row_index in range(len(matrix) - submatrix_size + 1):
#         for col_index in range(len(matrix[0]) - submatrix_size + 1):
#             current_sum = sum_of_submatrix_2x2(matrix, row_index, col_index, submatrix_size)
#             if current_sum > best_sum:
#                 best_sum = current_sum
#                 best_col_index = col_index
#                 best_row_index = row_index
#     return best_row_index, best_col_index,
#
#
# def print_result(coordinates, size):
#     (row_index, col_index) = coordinates
#     for r in range(row_index, row_index + size):
#         row = []
#         for c in range(col_index, col_index + size):
#             row.append(matrix[r][c])
#         print(' '.join(str(x) for x in row))
#     print(sum_of_submatrix_2x2(matrix, row_index, col_index, size))
#
#
# SUBMATRIX_SIZE = 2
#
# matrix = read_matrix(is_test=True)
# coordinates = iterate_over_real_matrix(matrix, SUBMATRIX_SIZE)
# print_result(coordinates, SUBMATRIX_SIZE)
