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

def histogram_list(word_list):
    histogram = []
    hist = []

    for word in word_list:
        if word not in histogram:
            histogram.append(word)
    
    for x in range(0, len(histogram)):
        frequency = word_list.count(histogram[x])
        pair = [histogram[x], frequency]
        hist.append(pair)
    
    return hist

def histogram_tuple(word_list):
    histogram = []
    hist = []

    for word in word_list:
        if word not in histogram:
            histogram.append(word)
    
    for x in range(0, len(histogram)):
        frequency = word_list.count(histogram[x])
        pair = (histogram[x], frequency)
        hist.append(pair)
    
    return hist

def histogram_count(word_list):
    hist = histogram_dictionary(word_list)
    values = sorted(hist.values())
    values_set = set(values)

    count_hist = []

    for val in values_set:
        words = []
        for key in hist:
            if hist[key] == val:
                words.append(key)
        count_hist.append((val, words))
    
    return count_hist

def unique_words(histogram):
    return len(histogram.keys())

def frequency(word, histogram):
    return histogram[word]

def main():
    text = 'sherlock_no_title_chapters.txt'
    word_list = generate_word_list(text)
    histo = histogram_dictionary(word_list)
    print(histo)
    print(unique_words(histo))
    print(frequency("skylight", histo))

if __name__== "__main__":
  main()