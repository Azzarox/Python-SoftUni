def palindrome(element):
    reversed_number = element[::-1]
    if element == reversed_number:
        return True
    return False


def separate_elements(text, sep):
    separated_list = text.split(sep)
    return separated_list


data = input()
list_of_sep_elem_functions = separate_elements(data, ", ")

for el in list_of_sep_elem_functions:
    print(palindrome(el))
W