# def read_matrix(count):
#     return [[int(x) for x in input().split(", ")] for _ in range(count)]  # making matrix
#
#
# def primary_diag(count):
#     return [matrix[i][i] for i in range(count)]  # returns list with the primary diagonal numbers
#
#
# def secondary_diag(count):
#     return [matrix[i][count - 1 - i] for i in range(count)]  # returns list with the secondary diagonal numbers
#
#
# def print_result():
#     print(f'First diagonal: {", ".join([str(el) for el in first_diag])}. Sum: {sum(first_diag)}')
#     print(f'Second diagonal: {", ".join([str(el) for el in sec_diag])}. Sum: {sum(sec_diag)}')
#
#
# count = int(input())
# matrix = read_matrix(count)
#
# first_diag = primary_diag(count)
# sec_diag = secondary_diag(count)
#
# print_result()

# def create_row(): # function for row and parsing it to int
#     row = input().split(", ")
#     return [int(x) for x in row]


n = int(input())

matrix = [[int(x) for x in input().split(", ")] for row in range(n)]
# matrix = [create_row() for _ in range(n)]  # comprehension with the function

primary_diagonal = [matrix[row_index][col_index]
                    for row_index in range(n)
                    for col_index in range(n)
                    if row_index == col_index]

secondary_diagonal = [matrix[row_index][col_index]
                      for row_index in range(n)
                      for col_index in range(n)
                      if n - 1 - row_index == col_index]

print(f'First diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Second diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')
