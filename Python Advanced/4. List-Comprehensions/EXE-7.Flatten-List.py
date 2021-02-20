# TODO: от презентацията
# преподавател: Велизар Шулев
matrix = [el.split() for el in input().split("|")]  # директно връща матрица

output_list = [element                              # връща  лист с обърнатите row-овете
               for row in reversed(matrix)
               for element in row
               ]

print(*output_list)                                 # разопаковаме листът

# output_list
# # ugly af - 75/100 - mine
# numbers = input().split("|")
# matrix = [[numbers[index].split() for index in range(len(numbers))][::-1][row] for row in range(len([numbers[index].split() for index in range(len(numbers))]))]
# print(*[" ".join(matrix[index]) for index in range(len(matrix))])

#
# original - mine - 75/100 time limit

# numbers = input().split("|")
# matrix = [numbers[index].split() for index in range(len(numbers))]
# reversed_matrix = [matrix[::-1][row] for row in range(len(matrix))]
# print(*[" ".join(reversed_matrix[index]) for index in range(len(reversed_matrix))])

# with normal for loop 75/100

# numbers = input().split("|")
# matrix = [numbers[index].split() for index in range(len(numbers))]
#
# for row in range(len(matrix)):
#     print(*matrix[::-1][row], end=" ")


# test only
# the matrix that is created
# [
#     ['1', '2', '3'],
#     ['4', '5', '6'],
#     ['7', '8'],
# ]
