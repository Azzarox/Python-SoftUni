# от презентацията

# rows, cols = [int(x) for x in input().split()]
#
# result = [[f"{chr(num)}{chr(nested_num)}{chr(num)}"for nested_num in range(num ,num+cols)] for num in range(97,97+rows)]
#
# print(*[" ".join(iterable) for iterable in result], sep="\n")

from string import ascii_lowercase


def create_cell(i, j):
    first_char = ascii_lowercase[i % 26]
    middle_char = ascii_lowercase[(i + j) % 26]
    return f'{first_char}{middle_char}{first_char}'


row, col = [int(x) for x in input().split()]

matrix = [create_cell(i, j)
          for i in range(row)
          for j in range(col)
          ]

print(*["".join(iterable) for iterable in matrix], sep="\n")  # не принтира както е трябва в задачата
