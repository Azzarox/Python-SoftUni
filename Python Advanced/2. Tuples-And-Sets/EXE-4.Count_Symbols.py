# solo best written

def main(input_line):
    counts = {}
    for ch in input_line:
        if ch not in counts:
            counts[ch] = 0
        counts[ch] += 1
    return counts


def sort_dict(counts_dict):
    return sorted(counts_dict.items())


def print_result(counts_dict):
    sorted_dict = sort_dict(counts_dict)
    for (letter, count) in sorted_dict:
        print(f'{letter}: {count} time/s')


# counts_dictionary = main("SoftUni rocks") # test hardcoded
counts_dictionary = main(input())
print_result(counts_dictionary)



# more messy code
#
# def main(line):
#     counts = {}
#     for ch in line:
#         if ch not in counts:
#             counts[ch] = 0
#         counts[ch] += 1
#     return counts
#
#
# def sort_dict(counts_dict):
#     return sorted(counts_dict.items())
#
#
# def print_result(sorted_dict):
#     for (letter, count) in sorted_dict:
#         print(f'{letter}: {count} time/s')
#
#
# result = main(input())
# # result = main("SoftUni rocks")
# print_result(sort_dict(result))