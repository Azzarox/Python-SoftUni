def input_lines(count):
    lines = set()
    for _ in range(count):
        data = input().split()
        for el in data:  # след като сплитнем получаваме лист и въртим през всеки елемент за да го добавим в set-а
            lines.add(el)
    return lines


def print_result(res):
    for el in res:
        print(el)


result = input_lines(int(input()))
print_result(result)
