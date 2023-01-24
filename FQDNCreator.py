# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 11:03:51 2021

@author: cengelbr
"""

import tkinter
from tkinter import filedialog
import re
import sys
import os

infile = filedialog.askopenfilename(
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

with open(infile, 'r') as readerIO:
    with open("fixedregex.txt", 'w+') as outfile:
        for line in readerIO:
            line = line.strip('\n')
            outfile.write('edit '+line+'\n')
            outfile.write('set type fqdn\n')
            outfile.write('set fqdn '+line+'\n')
            outfile.write('next\n')

readerIO.close()
outfile.close()

