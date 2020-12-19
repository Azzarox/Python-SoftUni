# Without watching anything - completely solo - awesome - 100/100 - text_processing

password = input()

line = input()
while not line == "Reveal":
    data = line.split(":|:")
    command = data[0]
    if command == "InsertSpace":
        index = int(data[1])
        password = password[:index] + " " + password[index:]
        print(password)
    elif command == "Reverse":
        substring = data[1]
        sub_reverse = substring[::-1]
        if substring in password:
            password = password.replace(substring, "", 1)  # replace only the first occurence
            password += sub_reverse
            print(password)
        elif substring not in password:
            print("error")
    elif command == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        password = password.replace(substring, replacement)
        print(password)

    line = input()

print(f'You have a new text message: {password}')
