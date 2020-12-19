def odd_even(num):
    string_of_num = str(num)
    odd = []
    even = []
    for char in string_of_num:
        if int(char) % 2 == 0:
            even.append(int(char))
        else:
            odd.append(int(char))
    total_odd = sum(odd)
    total_even = sum(even)

    return f'Odd sum = {total_odd}, Even sum = {total_even}'


number = int(input())
print(odd_even(number))
