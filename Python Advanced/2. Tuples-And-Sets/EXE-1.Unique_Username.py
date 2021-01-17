# with functions

def input_to_set(count):
    set_of_names = set()
    for _ in range(count):
        set_of_names.add(input())
    return set_of_names


def print_result(names):
    for name in names:
        print(name)


n = int(input())
data = input_to_set(n)

print_result(data)
