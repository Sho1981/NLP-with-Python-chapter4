# -*- coding: utf-8 -*-
import nltk

def prefix_only(key, word1, word2):
    """
    Return word1 is or isn't only word that include key.
    Type of key, word1 and word2 are str, and word1 and word2 are sorted.
    """
    assert isinstance(key, str) and isinstance(word1, str)\
            and isinstance(word2, str),"Please input str parameter."
    w1 = word1.find(key)
    w2 = word2.find(key)
    
    if w1 == 0 and  w2 != 0:
        return word1
    elif w1 != 0 and w2 == 0:
        return word2
    elif w1 == 0 and w2 == 0:
        return 'Many'
    else:
        return 'NONE'

def lookup(trie, key):
    """
    Return word if key in trie.
    Type of trie = set or list and key is str
    """
    assert isinstance(trie, list) and isinstance(key, str),\
                                "Please input (set or list, str) parameter."
    if len(trie) == 1:
        return prefix_only(key, trie[0], '')
    elif len(trie) == 2:
        return prefix_only(key, trie[0], trie[1])
    trie_sorted = sorted(trie)
    c = int(len(trie_sorted) * 0.5)
    trie1 = trie_sorted[:c]
    trie2 = trie_sorted[c:]   
    if key < trie1[-1]:
        return lookup((trie1+[trie2[0]]), key)
    elif key > trie2[0]:
        return lookup(trie2, key)
    elif key == trie1[-1] and key <= trie2[0]:
        return prefix_only(key, trie1[-1], trie2[0])
    elif key > trie1[-1] and key <= trie2[0]:
        return prefix_only(key, trie2[0], trie2[1])
    else:
        return 'NONE'

trie = ['some', 'any', 'every', 'each', 'all', 'no', 'something', 'anything']
key = 'an'

print(lookup(trie, key))
