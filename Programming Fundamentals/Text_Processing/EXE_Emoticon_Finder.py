string_data = input()

i = 0
while i <= len(string_data):
    if i == len(string_data):
        break
    if string_data[i] == ":" in string_data:
        print(string_data[i] + string_data[i+1])

    i += 1
