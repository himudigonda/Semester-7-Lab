#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Imports
import tokenize
import os

#Logic
'''
Select individual files -> Remove Lines till .W -> Tokenize -> Remove lines starting with . -> Remove Stop Words -> Find 30 Most Used Words
'''

for filename in os.listdir('../files'):
    with open(os.path.join("../files",filename), "r+") as f:
        text = f.read()
        # remove the first few lines
        text_in_file = text.split("\n")
        for i in range(len(text_in_file)):
            if text_in_file[i] == '.W':
                break
            text_in_file.pop(i)
        print(text_in_file)
