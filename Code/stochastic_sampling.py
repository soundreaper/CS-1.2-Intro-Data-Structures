from histogram import histogram
import random
import sys

f = open('sherlock_no_title_chapters.txt')
book = "one fish two fish red fish blue fish"

def random_selection(word_list):
    choice = random.choice(word_list)
    return choice[0]

def main():
    histo = histogram(book)
    print(random_selection(histo))

if __name__== "__main__":
  main()