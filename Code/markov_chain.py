from histogram import generate_word_list
import dictogram
import sys
import random

class MarkovChain:
    def __init__(self, file):
        self.word_list = generate_word_list(file)
        self.markov = self.make_chain(self.word_list)
    
    def make_chain(self, word_list):
        markov = {}

        for i in range(len(word_list)):
            if word_list[i] not in markov:
                markov[word_list[i]] = []
            if i < len(word_list) - 1:
                markov[word_list[i]].append(word_list[i + 1])

        for key in markov:
            markov[key] = dictogram.Dictogram(markov[key])

        return markov
    
    def walk_through(self, length):
        sentence = []
        sentence.append(random.choice(tuple(self.markov.keys())))

        for i in range(length-1):
            sentence.append(self.markov[sentence[i]].sample())

        string = ""
        for word in sentence:
            string += word + " "

        return string

def main(file, number):
    markov = MarkovChain(file)
    return markov.walk_through(number)

if __name__ == '__main__':
    main('sherlock_no_title_chapters.txt', 10)