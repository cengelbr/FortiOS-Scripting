# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:31:03 2021

@author: ac81851
"""

import os
import re
import sys
import tkinter
from tkinter import filedialog

def GroupGenny():
    infile = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
    
    holderstring = 'append member '
    
    with open(infile, 'r') as readerIO:
        holder = readerIO.read()
        holder = holder.split('\n')
        with open ('groupscript.txt', 'w+') as outfile:
            for line in holder:
                line = line.strip(' \n')
                if "/" not in line:
                    line = line + "/32"
                line = '"'+line+'"'
                holderstring = holderstring + line + ' '
            outfile.write(holderstring)
            
    readerIO.close()
    outfile.close()
    
    

GroupGenny()
