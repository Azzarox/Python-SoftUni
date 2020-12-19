first_word = input()
second_word = input()

second_word.replace(first_word, "")
while first_word in second_word:
    second_word = second_word.replace(first_word, "")  # .replace() must be stored in a variable

print(second_word)
