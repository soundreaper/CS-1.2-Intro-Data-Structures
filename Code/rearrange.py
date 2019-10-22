import sys
import random

words = []

for x in sys.argv[1:]:
    words.append(x)

random.shuffle(words)
print(*words)