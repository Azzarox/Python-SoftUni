# my code solo

def read_matrix():
    rows_count, cols_count = map(int, input().split())
    matrix = []
    for row_index in range(rows_count):
        row = [el for el in input().split()]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row_index in range(len(matrix)):
        row = []
        for col_index in range(len(matrix[0])):
            row.append(matrix[row_index][col_index])
        print(" ".join(str(x) for x in row))


matrix = read_matrix()

line = input()
while line != "END":
    data = line.split()
    if "swap" not in data or len(data) != 5:
        line = input()
        print("Invalid input!")
        continue

    command = data[0]
    if command == "swap":
        data = [int(el) for el in data[1:]]
        try:
            matrix[data[0]][data[1]], matrix[data[2]][data[3]] = matrix[data[2]][data[3]], matrix[data[0]][data[1]]
            print_matrix(matrix)
        except IndexError:
            print("Invalid input!")

    line = input()
