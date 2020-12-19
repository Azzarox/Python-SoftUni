# Without watching anything - completely solo - awesome - 90/100 - regex


import re

text = input()
pattern = r'(@|#)(?P<word_1>[a-zA-Z]{3,})\1(@|#)(?P<word_2>[a-zA-Z]{3,})\1'

matches = re.finditer(pattern, text)

valid_pairs = 0
valid_words = ""
mirror_words_list = []
not_mirror = True

for match in matches:
    word_dict = match.groupdict()

    valid_pairs += 1
    if word_dict["word_1"] == word_dict["word_2"][::-1]:
        valid_words = word_dict["word_1"] + " <=> " + word_dict["word_2"]
        mirror_words_list.append(valid_words)
        not_mirror = False

if valid_pairs == 0:
    print('No word pairs found!')

if valid_pairs >= 1:
    print(f'{valid_pairs} word pairs found!')

if not_mirror:
    print('No mirror words!')
elif not not_mirror:
    print('The mirror words are:')
    print(', '.join(mirror_words_list))
