n = int(input())

words = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in words:
        words[word] = [synonym]
    else:
        words[word].append(synonym)

for key, value in words.items():
    print(f'{key} - {", ".join(value)}')
