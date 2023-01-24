# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:26:07 2021

@author: AC81851
"""


import tkinter
from tkinter import filedialog
import xlrd



infile = filedialog.askopenfilename()

wb = xlrd.open_workbook(infile)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

with open('IPaddys.txt', 'w+') as outfile:
    outfile.write('config firewall address\n')
    for i in range(sheet.nrows):
        bit = sheet.cell_value(i, 0)
        outfile.write('edit "'+ bit +'/32"\n')
        outfile.write('set subnet '+bit+'/32\n')
        outfile.write('set comment "CTLC0031238"\n')
        outfile.write('next\n')
    outfile.write('end')
    outfile.close()
    
with open('IPgroup.txt', 'w+') as outfile2:
    outfile2.write('config firewall addrgrp\n')
    outfile2.write('edit "Zoom_IP_Group"\n')
    outfile2.write('append member')
    for i in range(sheet.nrows):
        bit = sheet.cell_value(i, 0)
        outfile2.write(' "'+bit+'/32"')
    outfile2.write('next\n')
    outfile2.write('end\n')
    outfile2.close()
    

    


