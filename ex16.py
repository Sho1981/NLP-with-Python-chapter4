# -*- coding: utf-8 -*-
import nltk
import re
import random

letter_vals = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 80, 'g': 3,
'h': 8, 'i': 10, 'j': 10, 'k': 20, 'l': 30, 'm': 40, 'n': 50, 'o': 70,
'p': 80, 'q': 100, 'r': 200, 's': 300, 't': 400, 'u': 6, 'v': 6, 'w': 800,
'x': 60, 'y': 10, 'z': 7}

letter_vals_list = sorted(letter_vals.items(), key=lambda item: item[1])

def gematria(word):
    """
    Return number sumed gematria values of word.
    Type of word is string
    """
    assert isinstance(word, str), "Please input string parameter."
    return sum(letter_vals[chr] for chr in word.lower()
                                if re.match(r'[a-zA-Z]+', chr))

def maxid(gem, stid):
    if gem == 1:
        return 0
    else:
        for i in reversed(range(stid+1)):
            if gem >= letter_vals_list[i][1]:
                return i

def decord_one(gem, mxid):
    id = random.randint(0, mxid)
    return letter_vals_list[id][0], gem - letter_vals_list[id][1]

def decode(word):
    """
    """
    assert isinstance(word, str), "Please input string parameter."
    gem = gematria(word)
    stdi = 25
    decode_word = ''
    while gem > 0:
        stdi = maxid(gem, stdi)
        chr, gem = decord_one(gem, stdi)
        #print('chr=%s, gem=%d, stid=%d' % (chr, gem, stdi))
        decode_word += chr
    return decode_word

word = 'random'
print('%s -> (decode) %s' % (word, decode(word)))

'''
for fileid in nltk.corpus.state_union.fileids():
    print('%19s: %dwords' % (fileid, 
                len([w for w in nltk.corpus.state_union.words(fileid)
                if gematria(w) == 666])))
'''