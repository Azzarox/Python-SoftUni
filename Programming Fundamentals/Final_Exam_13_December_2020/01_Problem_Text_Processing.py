username = input()

data = input()
while not data == "Sign up":
    command_data = data.split() # check if 1 space
    command = command_data[0]
    if command == "Case":
        case = command_data[1]
        if case == "upper":
            username = username.upper()
            print(username)
        elif case == "lower":
            username = username.lower()
            print(username)
    elif command == "Reverse":
        start_index = int(command_data[1])
        end_index_inclusive = int(command_data[2])
        if not (start_index or end_index_inclusive) in range(len(username)): # if don't use "not in" followed by brackets "( )" it breaks
            data = input()
            continue
        substring = username[start_index:end_index_inclusive+1]
        reverse_substring = substring[::-1]
        print(reverse_substring)
    elif command == "Cut":
        substring = command_data[1]
        string = ''
        if substring not in username:
            print(f"The word {username} doesn't contain {substring}.")
        elif substring in username:
            username = username.replace(substring, "") # check if only 1 or what
            print(username)
    elif command == "Replace": # check if should print if char not in string
        char = command_data[1]
        if char in username:
            username = username.replace(char, "*")
            print(username)
    elif command == "Check":
        char = command_data[1]
        if char in username:
            print("Valid")
        elif char not in username:
            print(f'Your username must contain {char}.')
    data = input()
