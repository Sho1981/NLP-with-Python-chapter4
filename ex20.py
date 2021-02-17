# -*- coding: utf-8 -*-
import nltk

def sorted_word_fq(words):
    """
    Return word list sorted by frequency in word list
    Type of words is list
    """
    assert isinstance(words, list), "Please input list parameter."
    fd = nltk.FreqDist(words)
    sorted_list = sorted([(w, fd[w]) for w in fd], key=lambda item: item[1],\
                reverse=True)
    return [w for w,_ in sorted_list]

raw = 'I am hero. I say yes.'
print(sorted_word_fq(nltk.word_tokenize(raw)))
