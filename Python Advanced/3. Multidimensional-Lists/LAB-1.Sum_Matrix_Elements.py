# my code solo

def read_matrix(rows_count, columns_count):
    matrix_inp = []
    for row in range(rows_count):
        rows = [int(x) for x in input().split(", ")]
        matrix_inp.append(rows)
    return matrix_inp


def sum_matrix(matrix):
    matrix_sum = 0
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[0])):
            matrix_sum += matrix[row_index][col_index]
    return matrix_sum


r, c = map(int, input().split(", "))
matrix = read_matrix(r, c)
print(sum_matrix(matrix))
print(matrix)

# TODO: от презентацията

# def read_matrix(is_test=False):
#     if is_test:
#         return [
#             [7, 1, 3, 3, 2, 1],
#             [1, 3, 9, 8, 5, 6],
#             [4, 6, 7, 9, 1, 0],
#         ]
#     else:
#         (rows_count, cols_count) = map(int, input().split(", "))
#         matrix = []
#         for row_index in range(rows_count):
#             row = [int(x) for x in input().split(", ")]
#             matrix.append(row)
#         return matrix
#
#
# def calculate_matrix_sum(matrix):
#     matrix_sum = 0
#
#     for r in range(len(matrix)):
#         row = matrix[r]
#         for c in range(len(row)):
#             matrix_sum += row[c]
#
#     return matrix_sum
#
#
# matrix = read_matrix()
# result = calculate_matrix_sum(matrix)
# print(result)
# print(matrix)
