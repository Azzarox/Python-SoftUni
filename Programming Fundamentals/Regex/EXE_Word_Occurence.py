import re

sentence = input()
text = input()

pattern = rf'\b{text}\b'
matches = re.findall(pattern, sentence, re.IGNORECASE) # returns list of the matches

print(len(matches))