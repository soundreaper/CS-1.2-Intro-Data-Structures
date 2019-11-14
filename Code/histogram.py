import sys
import random
import string

def generate_word_list(source_text):
    book = open(source_text).read()
    book = book.lower()
    for check in string.punctuation:
        book = book.replace(check, "")
    book = book.replace('“', '')
    book = book.replace('”', '')
    book = book.replace('’', '')
    book = book.replace('‘', '')
    book = book.replace('—', ' ')    
    book = book.split()

    return book

def histogram_dictionary(word_list):
    histogram = {}
    for word in word_list:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    
    return histogram
    
    # dup_check = []
    # word_count_list = []

    # for x in source_list:
    #     if x not in dup_check:
    #         dup_check.append(x)

    # for x in range(0, len(dup_check)):
    #     word_freq = source_list.count(dup_check[x])
    #     pair = [dup_check[x], word_freq]
    #     word_count_list.append(pair)
    
    # return(word_count_list)

def unique_words(histogram):
    return len(histogram.keys())
    # unique_word_count = 0
    # for x in histogram:
    #     unique_word_count += 1
    
    # print(unique_word_count)

def frequency(word, histogram):
    return histogram[word]
    # for x in histogram:
    #     if word == x[0]:
    #         print(x[1])

def main():
    text = 'sherlock_no_title_chapters.txt'
    word_list = generate_word_list(text)
    histo = histogram_dictionary(word_list)
    print(histo)
    print(unique_words(histo))
    print(frequency("skylight", histo))

if __name__== "__main__":
  main()