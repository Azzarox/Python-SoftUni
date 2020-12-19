data = input().split("\\")

file = data[-1]
file_name = file.split('.')

print(f'File name: {file_name[0]}')
print(f'File extension: {file_name[1]}')
