import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make text string from them."""

        corpus = ""
        # return a single string concatenated from multiple files
        for file_path in filenames:
            text = open(file_path).read()
            corpus += text
        self.make_chains(corpus)

    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""

        chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)

            # or we could say "chains.setdefault(key, []).append(value)"

        self.chains = chains


    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(chains.keys())
        words = [key[0], key[1]]
        while key in chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)

        return " ".join(words)

    def __init__(self):
        pass

if __name__ == "__main__":
    #print sys.argv
    # we should get list of filenames from sys.argv
    filenames = sys.argv[1:]
    # we should make an instance of the class
    g = SimpleMarkovGenerator()
    # we should call the read_files method with the list of filenames
    g.read_files(filenames)
    # we should call the make_text method 5x
   
    print g.make_text(g.chains)
