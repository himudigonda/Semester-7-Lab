#!/Users/himansheeeesh/anaconda3/bin/python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from nltk.tokenize import sent_tokenize, wordpunct_tokenize

# Global Variables
tokens = []

# Dataset Import
f = open('./cran/cran.all.1400')
data_unprocessed = f.read()

# Tokenization using NLTK
print(type(data_unprocessed))
print(sent_tokenize(data_unprocessed))
print(wordpunct_tokenize(data_unprocessed))

# Tokenization using For Loops

data_split_space = data_unprocessed.split()

for word in data_split_space:
    tokens.append(word)

print(tokens)
