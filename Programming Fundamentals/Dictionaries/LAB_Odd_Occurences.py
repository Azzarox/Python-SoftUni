words = input().split()

occurrences = {}

words = [word.lower() for word in words]

for word in words:
    occurrences[word] = words.count(word)

for key, value in occurrences.items():
    if not value % 2 == 0:
        print(key, end=" ")