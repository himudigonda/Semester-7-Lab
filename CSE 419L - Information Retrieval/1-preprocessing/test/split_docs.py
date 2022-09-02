#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
import re

#Logic
lines_per_file = 300
mini_file = None
file_name = 0
with open('cran.all.1400') as main_file:
    for lineno, line in enumerate(main_file):
        file_name += 1
        if re.findall(".I\s[0-9]", line):
            if mini_file:
                mini_file.close()
            mini_filename = '{}.txt'.format(file_name)
            mini_file = open(mini_filename, "w")


        #if lineno % lines_per_file == 0:
        #    if mini_file:
        #        mini_file.close()
        #    mini_filename = '{}.txt'.format(file_name)
        #    mini_file = open(small_filename, "w")
        mini_file.write(line)
    if mini_file:
        mini_file.close()
