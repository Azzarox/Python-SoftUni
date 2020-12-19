def password(text):
    word = True
    if not 6 <= len(text) <= 10:
        print("Password must be between 6 and 10 characters")
        word = False

    for char in text:
        if not char.isdigit():
            if not char.isalpha():
                word = False
                print(f'Password must consist only of letters and digits')
                break
    counter = 0
    for char in text:
        if char.isdigit():
            counter += 1
    if counter < 2:
        word = False
        print(f'Password must have at least 2 digits')

    return word


characters = input()
result = password(characters)

if result:
    print("Password is valid")

