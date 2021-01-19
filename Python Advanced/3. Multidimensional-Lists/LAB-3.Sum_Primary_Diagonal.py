def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
        ]
    else:
        matrix = []
        size = int(input())
        for row_index in range(size):
            row = [int(el) for el in input().split()]
            matrix.append(row)
        return matrix


def calc_primary_diagonal(matrix):
    primary_diagonal = 0
    for r in range(len(matrix)):
        primary_diagonal += matrix[r][r]

    return primary_diagonal


matrix = read_matrix()
res = calc_primary_diagonal(matrix)
print(res)
