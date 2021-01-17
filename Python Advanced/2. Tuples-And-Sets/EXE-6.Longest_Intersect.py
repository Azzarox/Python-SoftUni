# with functions - better and more understandable, but more lines of code

def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


def main(inp_data):
    intersections = []
    for el in inp_data:
        set_1, set_2 = el.split("-")
        start_1, stop_1 = map(int, set_1.split(","))
        start_2, stop_2 = map(int, set_2.split(","))

        start_1_range = range(start_1, stop_1 + 1)
        start_2_range = range(start_2, stop_2 + 1)

        set_1_set = set(start_1_range)
        set_2_set = set(start_2_range)

        intersection = set_1_set.intersection(set_2_set)
        intersections.append(intersection)

    return intersections


def sort_func(intersections):
    longest = sorted(intersections, key=lambda x: -len(x))[0]
    return longest


def print_res(longest):
    print(f'Longest intersection is {list(longest)} with length {len(longest)}')


n = int(input())
input_data = input_to_list(n)
intersections_list = main(input_data)
sorting_intersections_list = sort_func(intersections_list)
print_res(sorting_intersections_list)

print_res((sort_func(main(input_to_list(n))))) # the whole functions calling in one line


# without functions - more messy and harder to get the idea of it, but less code lines

# n = int(input())
# data = []
# for _ in range(n):
#     data.append(input())
#
# intersections = []
# for el in data:
#     set_1, set_2 = el.split("-")
#     start_1, stop_1 = map(int, set_1.split(","))
#     start_2, stop_2 = map(int, set_2.split(","))
#
#     start_1_range = range(start_1, stop_1 + 1)
#     start_2_range = range(start_2, stop_2 + 1)
#
#     set_1_set = set(start_1_range)
#     set_2_set = set(start_2_range)
#
#     intersection = set_1_set.intersection(set_2_set)
#     intersections.append(intersection)
#
# longest = sorted(intersections, key=lambda x: -len(x))[0]
#
# print(f'Longest intersection is {list(longest)} with length {len(longest)}')

