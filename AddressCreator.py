# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:46:48 2021

@author: ac81851
"""

"""IP Genny"""

import os
import re
import sys
import tkinter
from tkinter import filedialog

def AddrGenny():
    infile = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    
    with open(infile, 'r') as readerIO:
        holder = readerIO.read()
        holder = holder.split('\n')
        with open("addrscript.txt", 'w+') as outfile:
            for line in holder:
                line = line.strip('\n')
                line = line.strip(' ')
                if "/" not in line:
                    line = line + "/32"
                
                outfile.write('edit "'+line+'"\n')
                outfile.write('set subnet '+line+'\n')
                outfile.write('set comment "RITM0018358, 2022-11-17"\n')
                outfile.write('next\n')
    
    readerIO.close()
    outfile.close()

    
AddrGenny()
