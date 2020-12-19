data_string = list(input())

chars = []

while True:
    if data_string[0] == len(data_string) + 1:
        break
    if data_string[0] != data_string[1]:
        if data_string[0] != data_string[1]:
            if data_string[0] != data_string[1] and len(data_string) == 2:
                chars.append(data_string[0])
                chars.append(data_string[1])
                break
            x = data_string.pop(0)
            chars.append(x)
            continue
    elif data_string[0] == data_string[1]:
        if data_string[0] == data_string[1] and len(data_string) == 2:
            chars.append(data_string[0])
            break
        data_string.pop(1)
        continue

print("".join(chars))

# pseudo notepad code for the last part aa or ab and so on
# a b
# 0 1
#
# data_string[0] = a
# data_string[1] = a
#
# chars = []
#
# if data_string[0] == data_string[1] and len(data_string) == 2:
# 	chars.append(data_string[0])
# 	break
# elif data_string[0] != data_string[1] and len(data_string) == 2:
# 	 chars.append(data_string[0])
# 	 chars.append(data_string[1])
# 	 break
#
# 0123456789
# aaaaabbbbbcdddeeeedssaa  step 1
# aaaabbbbbcdddeeeedssaa   step 2 if index 0 is equal to index 1 - pop index 1  => 4 "a"
# aaabbbbbcdddeeeedssaa    3 "a"
# aabbbbbcdddeeeedssaa     2 "a"
# abbbbbcdddeeeedssaa      step 3 if index 0 is not equal to index 1 - pop index 0 and save it as a not repeating character => we save "a"
# bbbbbcdddeeeedssaa       repeat steps until only 2 characters left
# aa                       step 4 if len is equal to 2 and index 0 and index 1 are equal => we save the index of 0
#                                                  (or 1 doesn't matter since they are equal) and break the program
# ab                       step 5 if len is equal to 2 and index 0 and index 1 are not equal => we save both indeces and break the program
#
# abcdedsa