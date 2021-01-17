def input_lines_list(count):
    total = []
    for counter_line in range(1, count + 1):
        line = input()
        ord_value = sum([ord(ch) for ch in line])
        total.append(ord_value // counter_line)

    return total


def to_odd_or_even(data):
    even = set()
    odd = set()

    for num in data:
        if num % 2 == 0:
            even.add(num)
        else:
            odd.add(num)

    return even, odd, sum(even), sum(odd)


def check_if(set_1, set_2, sum_even, sum_odd):
    if sum_even == sum_odd:
        return set_1.union(set_2)
    if sum_odd > sum_even:
        return set_2.difference(set_1)
    if sum_even > sum_odd:
        return set_1.symmetric_difference(set_2)


def print_res(res):
    if check_if:
        print(', '.join(map(str, res)))


inp_data = input_lines_list(int(input()))
(even_set, odd_set, sum_set_even, sum_set_odd) = to_odd_or_even(inp_data)
result = check_if(even_set, odd_set, sum_set_even, sum_set_odd)
print_res(result)
