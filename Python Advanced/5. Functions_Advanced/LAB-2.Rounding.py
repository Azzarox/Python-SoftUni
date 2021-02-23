def turn_num(nums):
    return [float(num) for num in nums]


def round_nums(nums):
    return list(map(lambda x: round(x), nums))


numbers = turn_num(input().split())
result = round_nums(numbers)
print(result)