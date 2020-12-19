import re
text = input()

pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'  #\b[A-Z][a-z]+\s[A-Z][a-z]+\b    -> this regex detects more than 1 space

matches = re.findall(pattern, text)       # Returns a list of strings -> "".join()

print(" ".join(matches))

# for match in matches:                   # or you can get them from the list
#     print(match, end=' ')
