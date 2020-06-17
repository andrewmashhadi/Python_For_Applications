#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: Andrew Mashhadi
"""

#%% 1
def get_path(key, val, d):
    """ Returns the path starting from the input pair."""
    
    count = 1
    cur_val = val
    potential_keys = set(d.keys())
    potential_keys.remove(key)
    while True:     
        if cur_val in potential_keys:
            potential_keys.remove(cur_val)
            count += 1
            cur_val = d[cur_val]               
        else:
            break
    return count

def longest_path_length(d):
    """Returns the length of the longest path in d."""

    max_count = 0;
    for key, val in d.items():          
        cur_count = get_path(key, val, d)            
        if cur_count > max_count:
            max_count = cur_count
            
    return max_count

#%% 2
def large_value_keys(d, N):
    """Returns a list containing various keys in d.
    
    d is a dictionary who values are ints. N is an int.
    The list contains keys k whose corresponding value d[k] is bigger than N.
    The keys are arranged in order of largest value to smallest value.
    """
    
    pairs = list(d.items())
    ordered_pairs = sorted(pairs, key = lambda x: x[1], reverse = True)
    
    L = []
    for pair in ordered_pairs:
        if pair[1] > N :
            L.append(pair[0])
    
    return L

#%% 3
def get_non_alphas(data):
    """Returns a string of all the non-alphabetical characters."""
      
    words = data.split()        
    s = set()
    
    for word in words:
        if not word.isalpha():
            for letter in word:
                if not letter.isalpha():
                    s.add(letter)
    not_alphas = ''
    return not_alphas.join(s)
    
def count_words(filename):
    """Creates a dictionary from a .txt file counting word occurrences.
    
    For each word in the text file, there's a key.
    The corresponding value is the number of occurrences of the word.
    
    https://docs.python.org/3.7/library/stdtypes.html#string-methods
    
    Capitals are converted to lower case
    so that 'The' does not show up as a key.
    
    Dashes are replaced with spaces
    so that 'them—at' does not show up as a key.
    Both the short dash (-) and long dash (—) are dealt with.
    
    Non-alphabetic characters are stripped from words
    so that '“espionage?”' does not show up as a key.
    However, both "paper’s" and "papers" can show up as keys.
    """

    with open(filename, encoding='utf-8') as f:
        novel = f.read()
        
    non_alphas = get_non_alphas(novel)
        
    novel = novel.lower()   
    words = novel.split()
    d_words = dict()
    
    for word in words:    
        words_to_add = []
        if not word.isalpha():        
            new_str = word.replace("-", " ")
            new_str = new_str.replace("—", " ")
            for n_word in new_str.split():               
                n_word = n_word.strip(non_alphas)
                words_to_add.append(n_word)
        else:
            words_to_add.append(word)
     
        for a_word in words_to_add:
            if a_word in d_words:
                d_words[a_word] += 1
            else:
                d_words[a_word] = 1
            
    return d_words
