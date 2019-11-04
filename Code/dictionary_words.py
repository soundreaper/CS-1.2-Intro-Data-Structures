import sys
import random

sentence_length = int(sys.argv[1])

f = open('/usr/share/dict/words')
words = f.read().split("\n")

x = 0
sentence = []

while x < sentence_length:
    sentence.append(words[random.randint(0, len(words)-1)])
    x+=1

print(*sentence)