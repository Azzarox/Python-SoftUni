password = input()

line = input()
while line != "Done":

    data = line.split(" ")
    command = data[0]
    if command == "TakeOdd":
        new_pass = ""
        for char in range(1, len(password), 2):
            new_pass += password[char]
        password = new_pass
        print(new_pass)
    elif command == "Cut":
        index = int(data[1])
        length = int(data[2])
        password = password[:index] + password[index+length:]
        print(password)
    elif command == "Substitute":
        substring, substitute = data[1:]
        if substring not in password:
            print(f'Nothing to replace!')
        else:
            password = password.replace(substring, substitute)
            print(password)

    line = input()

print(f'Your password is: {password}')
