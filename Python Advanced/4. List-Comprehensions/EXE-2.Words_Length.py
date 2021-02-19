# the long

# text = input()
# text = {el: len(el) for el in text.split(", ")}  # dictionary comprehension  with the word and the len
# text = ", ".join([f"{el} -> {text[el]}" for el in text]) # list comprehension with the formatted string and .join()
# print(text)

# the short

text = {el: len(el) for el in input().split(", ")}
print(", ".join([f"{el} -> {text[el]}" for el in text]))

