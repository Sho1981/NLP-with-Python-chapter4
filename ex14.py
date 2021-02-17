import nltk

def novel10(text):
    """
    Print words in last 10% text not to aware first 90% text.
    type(text) = list
    """
    assert isinstance(text, list), "Please input parameter 'text' to list."

    cut = int(0.9 * len(text))
    forward, backward = text[:cut], text[cut:]
    wordlist = set(forward)
    print([w for w in backward if w not in wordlist])

raw = nltk.corpus.gutenberg.raw('austen-emma.txt')
novel10(nltk.word_tokenize(raw))
