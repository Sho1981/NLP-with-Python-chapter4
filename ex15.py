# -*- coding: utf-8 -*-
import nltk
import re
import pprint

def print_freq_words(text):
    """
    Print frequency of each word in text.
    Type of text is string
    """
    assert isinstance(text, str), "Please input parameter 'text' to string."
    
    sent = nltk.word_tokenize(text)
    fd = nltk.FreqDist(w.lower() for w in sent if re.match(r'[a-zA-Z0-9]',w))
    for w in fd:
        print('%12s, %3d' % (w, fd[w]))
#   pprint.pprint([(w, fd[w]) for w in fd])

raw = 'Take care of the sense, and the sounds will take care of themselves.'

print_freq_words(raw)