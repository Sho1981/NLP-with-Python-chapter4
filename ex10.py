# -*- coding: utf-8 -*-
"""
Sorting words in order of the length
"""
def cmp_len(words):
    """Sort words in order of the length"""

    return [w for _,w in sorted([(len(word), word)
                                  for word in words], reverse=True)]

sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
print(cmp_len(sent))
