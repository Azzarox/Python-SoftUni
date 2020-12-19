import re

text = input()

pattern = r"\+359([ -])2\1[0-9]{3}\1[0-9]{4}\b" # with group and backreference
# pattern = r"(\+359\s2\s\d{3}\s\d{4})|(\+359-2-\d{3}-\d{4}\b)" #ne stava s findall() zashtoto vrushta tuples

matches = re.finditer(pattern, text)            #finditer() returns match object

matches = [match.group() for match in matches]  #print the match.group() the full match and return it in a list so we can join by comma

print(', '.join(matches))
