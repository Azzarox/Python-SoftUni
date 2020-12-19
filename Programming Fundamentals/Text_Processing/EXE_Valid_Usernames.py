string_list = input().split(", ")
is_valid = True
third = False
list_of_valid = []

for element in string_list:
    if not len(element) in range(3, 17):
        is_valid = False
        continue
    elif not element.strip():
        is_valid = False
        continue
    else:
        if element.isalpha():
            third = True
            is_valid = True
        elif element.isdigit():
            third = True
            is_valid = True
        elif "-" in element:
            third = True
            is_valid = True
        elif "_" in element:
            third = True
            is_valid = True
    if not third:
        is_valid = False

    if is_valid:
        list_of_valid.append(element)

if is_valid:
    for name in list_of_valid:
        print(name)