import re

text = input()

pattern_user = r'( |^)[a-zA-Z[0-9]+((\.|\-|_)[a-zA-Z0-9]+)*'
pattern_host = r'[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+'

pattern = rf'{pattern_user}@{pattern_host}'

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())
