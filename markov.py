"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()

    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 1):
        try:
            if not chains.get((words[i], words[i + 1])):
                chains[(words[i], words[i + 1])] = [words[i + 2]]
                continue
            chains.get((words[i], words[i + 1])).append(words[i + 2])
        except IndexError:
            break

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    random_key = choice(list(chains))
    words.append(random_key[1])
    words.append(choice(list(chains.get(random_key))))

    while True:
        if (words[-2], words[-1]) in chains:
            new_key = chains[(words[-2], words[-1])]
            words.append(choice(list(new_key)))
            continue
        break

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
