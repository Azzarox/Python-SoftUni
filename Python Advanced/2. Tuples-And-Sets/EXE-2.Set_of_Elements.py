def main_make_set(data):
    n, m = data.split() # или може този split директно долу в извикването на функцията
    n = int(n)
    m = int(m)

    set_1 = set()
    set_2 = set()

    for _ in range(n):
        set_1.add(input())

    for _ in range(m):
        set_2.add(input())

    return set_1, set_2


def numbers_in_both_sets():
    ch_set = set()

    for ch in set_first:
        if ch in set_second:
            ch_set.add(ch)

    return ch_set


def print_result(res):
    for s in res:
        print(s)


set_first, set_second = main_make_set(input()) # това връща tuple и го разопаковам в set_first и set_second
result = numbers_in_both_sets()
print_result(result)
