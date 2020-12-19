string = input()
x_of_strings = string.split(' ')  # .split() returns list

# x = [int(i) for i in x]

x_of_integers = []
final_list = []
for i in x_of_strings:
    x_of_integers.append(int(i))
    for j in x_of_integers:
        if j > 0:
            j *= -1
        else:
            j *= -1

    final_list.append(j)

print(final_list)
