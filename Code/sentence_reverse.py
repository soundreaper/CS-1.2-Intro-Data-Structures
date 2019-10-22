import sys

sentence = []

for x in sys.argv[1:]:
    sentence.append(x)

reverse = sentence[::-1]

print(*reverse)