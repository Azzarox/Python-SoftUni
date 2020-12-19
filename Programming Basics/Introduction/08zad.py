length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume = length * width * height
littres = volume / 1000

result = littres * (1 - percent)
print(result)




