#!/Users/himansheeeesh/anaconda3/bin/python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
from nltk.tokenize import sent_tokenize, wordpunct_tokenize

# Global Variables
tokens = []


class tokenizer:
    
    def __init__(self, file):
        self.file = file
    
    def tokenize(self, file):
        pass
        f = open(file)
        data_unprocessed = f.read()
        data_split_space = data_unprocessed.split()
    
        for word in data_split_space:
            tokens.append(word)
    
        return(tokens)
