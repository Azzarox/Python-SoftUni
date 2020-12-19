# with slicing 100/100 - solo - check for dots in prints - text processing

activation_key = input()
validator_for_act_key = activation_key.isalnum()

data = input()

while not data == "Generate":
    command_data = data.split(">>>")
    command = command_data[0]
    if command == "Contains":
        substring = command_data[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')

        elif substring not in activation_key:
            print('Substring not found!')

    elif command == "Flip":
        up_low_case = command_data[1]
        start_index = int(command_data[2])
        end_index = int(command_data[3])

        substring = activation_key[start_index:end_index]  # the substring that I need to change
        beginning_new_string = activation_key[:start_index]
        ending_new_string = activation_key[end_index:]  # the main string without the substring

        if up_low_case == "Upper":
            substring = substring.upper()
        elif up_low_case == "Lower":
            substring = substring.lower()

        activation_key = beginning_new_string + substring + ending_new_string

        print(activation_key)

    elif command == "Slice":
        start_index = int(command_data[1])
        end_index = int(command_data[2])
        substring = activation_key[start_index:end_index]
        activation_key = activation_key[:start_index] + activation_key[end_index:]

        print(activation_key)

    data = input()

print(f"Your activation key is: {activation_key}")



# with .replace()
#
# 100/100 first judge try
# activation_key = input()
# validator_for_act_key = activation_key.isalnum()
#
# data = input()
#
# while not data == "Generate":
#     command_data = data.split(">>>")
#     command = command_data[0]
#     if command == "Contains":
#         substring = command_data[1]
#         if substring not in activation_key:
#             print('Substring not found!')
#         else:
#             print(f'{activation_key} contains {substring}')
#
#     elif command == "Flip":
#         up_low_case = command_data[1]
#         start_index = int(command_data[2])
#         end_index = int(command_data[3])
#         substring = activation_key[start_index:end_index]
#         if up_low_case == "Upper":
#             new_substring = activation_key[start_index:end_index].upper()
#         else:
#             new_substring = activation_key[start_index:end_index].lower()
#         activation_key = activation_key.replace(substring, new_substring)
#
#         print(activation_key)
#     elif command == "Slice":
#         start_index = int(command_data[1])
#         end_index = int(command_data[2])
#         substring = activation_key[start_index:end_index]
#         activation_key = activation_key.replace(substring, "")
#
#         print(activation_key)
#
#     data = input()
#
# print(f"Your activation key is: {activation_key}")