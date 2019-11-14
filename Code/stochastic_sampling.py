import histogram
import random
import sys

def random_selection(word_list):
    choice = random.choice(word_list)
    return choice

def sample_by_frequency(histogram):
    count = random.randint(1, sum(histogram.values()))

    for key in histogram:
        count -= histogram[key]
        if count <= 0:
            return key
    return -1

def main():
    book = 'sherlock_no_title_chapters.txt'
    word_list = histogram.generate_word_list(book)
    histo = histogram.histogram_dictionary(word_list)
    print(sample_by_frequency(histo))

if __name__== "__main__":
  main()