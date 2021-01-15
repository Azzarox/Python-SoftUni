# соло написани функции

def logic(data):
    # data = map(float, data) # или float(value) долу в принта
    counts = {}
    for num in data:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    return counts


def print_result(counts):
    for value, counts in counts.items():
        print(f'{float(value)} - {counts} times')


# result = logic("-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3".split()) # hardcoded test
result = logic(input().split())  # или да сложим map(float, input().split()) при извикването на функцията
print_result(result)

# без функции
#
# data = input().split()
#
# counts = {}
# for num in data:
#     if num not in counts:
#         counts[num] = 0
#     counts[num] += 1
#
# for (value, counts) in counts.items():
#     print(f'{float(value)} - {counts} times')


# TODO: от презентацията:
# values = map(float, input().split(' '))
#
# values_counts = {}
# for value in values:
#     if value not in values_counts:
#         values_counts[value] = 0
#     values_counts[value] += 1
#
# for (value, count) in values_counts.items():
#     print(f'{value} - {count} times')