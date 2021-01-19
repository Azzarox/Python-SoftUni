# my code solo

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
            rows = [int(el) for el in input().split()]
            matrix.append(rows)
        return matrix


def matrix_column_sum(matrix):
    columns = len(matrix[0])
    rows = len(matrix)

    matrix_column_sum_list = []
    for column_index in range(columns):
        matrix_sum = 0
        for rows_index in range(rows):
            matrix_sum += matrix[rows_index][column_index]

        matrix_column_sum_list.append(matrix_sum)

    return matrix_column_sum_list


def print_res(res):
    [print(el) for el in res]


matrix = read_matrix()
result = matrix_column_sum(matrix)
print_res(result)

#
# # TODO: от презентацията
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
#             row = [int(x) for x in input().split(' ')]
#             matrix.append(row)
#
#         return matrix
#
#
# def get_column_sums(matrix):
#     rows_count = len(matrix)
#     columns_count = len(matrix[0])
#
#     # sums = []
#     # for column_index in range(columns_count):                        # подобно на моето решение
#     #     sums.append(0)                                               # за да държи новите стойности на отделни индекси в sums- листа
#     #     for row_index in range(rows_count):
#     #         sums[-1] += matrix[row_index][column_index]              # [-1] защото е последният елемент, тъй като имаме append
#
#     sums = [0] * columns_count                                     # добавя 0-ли на columns_count (което е 6 в случая)
#     for row_index in range(rows_count):
#         for column_index in range(columns_count):
#             sums[column_index] += matrix[row_index][column_index]  # на индексът от columns_count добавя числото на matrix[row_index][column_index]
#                                                                    # и така се получава само 1 лист с len от 6
#     return sums
#
#
# def print_result(values):
#     [print(x) for x in values]
#
#
# matrix = read_matrix(is_test=True)
# result = get_column_sums(matrix)
# print_result(result)