# -*- coding: utf-8 -*-
import nltk

def shorten(text, n):
    """
    Return text remove words appeared over n times in text
    Type of text is str and n is int
    """
    assert isinstance(text, str) and isinstance(n, int),\
                                "Please input (str, int) parameter."
    words = nltk.word_tokenize(text)
    fd = nltk.FreqDist(words)
    hf_words = [w for w in words if fd[w] < n]
    return ' '.join(hf_words)

#raw = nltk.corpus.gutenberg.raw('austen-emma.txt')
raw = 'I am hero. I say yes.'
print(shorten(raw,2))
