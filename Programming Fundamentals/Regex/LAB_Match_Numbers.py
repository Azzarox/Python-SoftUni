import re

text = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern,text)

matches = [match.group() for match in matches]
print(' '.join(matches))

# for match in matches:
#     print(match.group(), end=' ')
