import math
numbers = list(map(int, input().split(", ")))

max_loop_range = math.ceil(max(numbers) / 10)
chars = []
for i in range(1, max_loop_range + 1):
    upper_limit = i * 10
    lower = upper_limit - 10

    chars = [ch for ch in numbers if lower < ch <= upper_limit]

    # for ch in numbers:
    #     upper_limit = i * 10
    #     lower = upper_limit - 10
    #     if lower < ch <= upper_limit:
    #         chars.append(ch)

    print(f"Group of {10 * i}'s: {chars}")

# to_check
