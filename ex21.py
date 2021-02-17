# -*- coding: utf-8 -*-
import nltk

def unexist_words(words, vocab):
    """
    Return word list that not exist in vocabulary list.
    Type of words and vocab is list
    """
    assert isinstance(words, list) and isinstance(vocab, list),\
                                "Please input list parameter."
    return set([w.lower() for w in words if w.lower() not in vocab])

raw = 'I am hero. I say yes. syoid'
print(unexist_words(
        [w for w in nltk.word_tokenize(raw)],\
        [w.lower() for w in set(nltk.corpus.words.words())]))

print(set([w.lower() for w in nltk.word_tokenize(raw)]).difference(\
        set([w.lower() for w in set(nltk.corpus.words.words())])))