str1 = input()  # bubble gum
str2 = input()  # turtle hum

for i in range(len(str1)):
    if str1[i] != str2[i]:
        for str2_index in range(0, i + 1):
            print(str2[str2_index], end='')
        for str1_index in range(i + 1, len(str1)):
            print(str1[str1_index], end='')
        print()
