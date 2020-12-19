import re

text = input()
# pattern = r'\b((_[a-z]+)|(_[a-z]+[A-Z]+[a-z]+))\b'  # don't match digits and its way uglier

pattern = r'\b_[A-Za-z0-9]+\b'       # without groups on regex
matches = re.findall(pattern, text)

matches_no_underscore = [match[1:] for match in matches]
print(",".join(matches_no_underscore))

# with group on regex
# 
# import re
# text = input()
# pattern = r'\b_([A-Za-z0-9]+)\b'
# matches = re.findall(pattern, text)
# print(",".join(matches))
