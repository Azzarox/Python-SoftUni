string = input().split()

for chars in string:
    word = chars * len(chars)  # The asterisk symbol multiplies string
    print(word, end="")
