#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Imports
from tokenizer import tokenizer
import os
import re

#Logic
'''
Select individual files -> Remove Lines till .W -> Tokenize -> Remove lines starting with . -> Remove Stop Words -> Find 30 Most Used Words
'''

reg = '.W'
class pipeline:
    def __init__(self) -> None:
        pass
    
    def pipeline(self):
        for filename in os.listdir('../files'):
            with open(os.path.join("../files",filename), "r+") as f:
                text = f.read()
                # remove the first few lines
                text_in_file = text.split("\n")
                for i in range(len(text_in_file)):
                    flag = re.findall(reg, text_in_file[i-1])
                    if flag:
                        break
                    else:
                        text_in_file.pop(i)

pipeline = pipeline()
pipeline.pipeline()
