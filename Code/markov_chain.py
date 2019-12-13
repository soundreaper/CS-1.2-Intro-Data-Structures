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

        n_words = len(word_list)
        for i, key1 in enumerate(word_list):
            if n_words > (i+2):
                key2 = word_list[i+1]
                word = word_list[i+2]
                if (key1, key2) not in markov:
                    markov[(key1, key2)] = [word]
                else:
                    markov[(key1, key2)].append(word)
        
        print('Corpus size: {0} words.'.format(len(word_list)))
        print('Chain size: {0} distinct word pairs.'.format(len(markov)))
        return markov

        # Old Code for 1st Order Markov Chain
        """
        markov = {}

        for i in range(len(word_list)):
            if word_list[i] not in markov:
                markov[word_list[i]] = []
            if i < len(word_list) - 1:
                markov[word_list[i]].append(word_list[i + 1])

        for key in markov:
            markov[key] = dictogram.Dictogram(markov[key])

        return markov
        """
    
    def walk_through(self):
        r = random.randint(0, len(self.word_list) - 1)
        key = (self.word_list[r], self.word_list[r + 1])
        tweet = key[0] + ' ' + key[1]

        while len(tweet) < 140:
            w = random.choice(self.markov[key])
            tweet += ' ' + w
            key = (key[1], w)

        return tweet.capitalize() + '.'
         
        # Old Code to Walk Through 1st Order Markov Chain
        """
        sentence = []
        sentence.append(random.choice(tuple(self.markov.keys())))

        for i in range(length-1):
            sentence.append(self.markov[sentence[i]].sample())

        string = ""
        for word in sentence:
            string += word + " "

        return string
        """

def main(file):
    markov = MarkovChain(file)
    return markov.walk_through()

if __name__ == '__main__':
    main('sherlock_no_title_chapters.txt')