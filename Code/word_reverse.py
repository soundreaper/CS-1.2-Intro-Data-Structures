import sys

words = []

for x in sys.argv[1:]:
    words.append(x)

reverse = []

for y in words:
    reverse.append(y[::-1])

print(*reverse)