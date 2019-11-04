import sys
import itertools

word = sys.argv[1]
print(*["".join(perm) for perm in itertools.permutations(word)])

"""
def all_permutations(word):
    if len(word) <= 1:
        print(word)
    else:
        temp = []
        for permumation in all_permutations(word[1:]):
                for i in range(len(word)):
                    temp.append(permumation[:i] + word[0:1] + permumation[i:])
        print(temp)

if __name__ == '__main__':
    test = 'ab'
    all_permutations(test)
"""