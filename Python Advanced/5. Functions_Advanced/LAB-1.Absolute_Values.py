def convert_to_int(inp):
    return [float(x) for x in inp]


def abs_value(values):
    return list(map(lambda x: abs(x), values))


numbers = convert_to_int(input().split())
result = abs_value(numbers)
print(result)