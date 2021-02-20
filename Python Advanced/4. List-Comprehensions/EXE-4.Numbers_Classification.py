# using functions as if statement

def turn_to_ints():
    return [int(el) for el in input().split(", ")]


def is_positive(x):
    return x >= 0


def is_negative(x):
    return x < 0


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return x % 2 != 0


def print_all(nums):
    print("Positive: " + ", ".join([str(el) for el in numbers if is_positive(el)]))
    print("Negative: " + ", ".join([str(el) for el in numbers if is_negative(el)]))
    print("Even: " + ", ".join([str(el) for el in numbers if is_even(el)]))
    print("Odd: " + ", ".join([str(el) for el in numbers if is_odd(el)]))

    # print(f'Positive: {", ".join([str(el) for el in numbers if is_positive(el)])}')  # with f-string is faster in judge 0.57s without 0.71
    # print(f'Negative: {", ".join([str(el) for el in numbers if is_negative(el)])}')
    # print(f'Even: {", ".join([str(el) for el in numbers if is_even(el)])}')
    # print(f'Odd: {", ".join([str(el) for el in numbers if is_odd(el)])}')


numbers = turn_to_ints()

print_all(numbers)


# using functions to return the comprehension with the if statement

# def turn_to_ints():
#     return [int(el) for el in input().split(", ")]
#
#
# def is_positive(nums):
#     return [x for x in nums if x >= 0]
#
#
# def is_negative(nums):
#     return [x for x in nums if x < 0]
#
#
# def is_even(nums):
#     return [x for x in nums if x % 2 == 0]
#
#
# def is_odd(nums):
#     return [x for x in nums if x % 2 != 0]
#
#
# def print_all(nums):
#     print(f'Positive: {", ".join(str(el) for el in is_positive(nums))}')
#     print(f'Negative: {", ".join(str(el) for el in is_negative(nums))}')
#     print(f'Even: {", ".join(str(el) for el in is_even(nums))}')
#     print(f'Odd: {", ".join(str(el) for el in is_odd(nums))}')
#
#
# numbers = turn_to_ints()
#
# print_all(numbers)
