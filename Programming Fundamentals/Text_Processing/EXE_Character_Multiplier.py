

# Similar , better code - 100/100 - from video

strings = input().split()
string_1 = strings[0]
string_2 = strings[1]

min_len = min(len(string_1), len(string_2))

result = 0
for i in range(min_len):
    result += ord(string_1[i]) * ord(string_2[i])

biggest_word = string_1
if len(string_2) > len(string_1):
    biggest_word = string_2

for i in range(min_len, len(biggest_word)):
    result += ord(biggest_word[i])

print(result)


# My code - Ugly af - 100/100 tho - little help from video

# strings = input().split()
#
# strings_1 = []
# strings_2 = []
#
# for el in strings[0]:
#     strings_1.append(ord(el))
#
# for el in strings[1]:
#     strings_2.append(ord(el))
#
# list_len_str = [len(strings_1), len(strings_2)]
#
# max_len = max(list_len_str)
# min_len = min(list_len_str)
#
# biggest_len_word = strings_1
# if len(strings_2) > len(strings_1):
#     biggest_len_word = strings_2
#
# result = 0
# for i in range(min_len):
#     result += strings_1[i] * strings_2[i]
#
# for i in range(min_len, max_len):
#     result += biggest_len_word[i]
#
# print(result)
