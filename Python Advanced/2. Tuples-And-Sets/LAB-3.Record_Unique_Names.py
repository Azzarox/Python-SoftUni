def input_to_set(count):
    lines = set()
    for _ in range(count):
        lines.add(input())
    return lines


def print_result(names):
    for name in name_set:
        print(name)


n = int(input())
name_set = input_to_set(n)
print_result(name_set)

# TODO: от презентацията

# def input_to_list(count):
#     lines = []
#     for _ in range(count):
#         lines.append(input())
#
#     return lines
#
#
# def print_result(names):
#     for name in names:
#         print(name)
#
#
# # names = [
# #     'Lyle',
# #     'Bruce',
# #     'Alice',
# #     'Easton',
# #     'Shawn',
# #     'Alice',
# #     'Shawn',
# # ]
#
# # unique_names = set(names)
#
# n = int(input())
# names = input_to_list(n)
# unique_names = set()
# for name in names:
#     unique_names.add(name)
# print_result(unique_names)
