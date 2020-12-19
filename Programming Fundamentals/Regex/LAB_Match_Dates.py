import re
text = input()

pattern = r'\b(?P<Day>\d{2})(?P<Sep>[\./-])(?P<Month>[A-Z][a-z]{2})(?P=Sep)(?P<Year>\d{4})\b' # -> to use match object .groupdict() with named groups

matches = re.finditer(pattern,text)
for match in matches:
    match_dict = match.groupdict()
    print(f'Day: {match_dict["Day"]}, Month: {match_dict["Month"]}, Year: {match_dict["Year"]}')



#first pattern pattern = r'\b\d{2}([./-])[A-Z][a-z]{2}\1\d{4}\b'
# 1st pattern logic #
# for match in matches: # conplex af -> split by group(1) since that is the separator;
#     x = match.group().split(mat1ch.group(1)) # group() is the full matches then split it by the group(1)
#     day = x[0]
#     month = x[1]
#     year = x[2]
#     print(f'Day: {day}, Month: {month}, Year: {year}')

