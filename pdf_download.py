#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:51:24 2017

@author: rembeza
"""
#to download pdf files with media listed in a 'results' file
#for many entries of the same microorganism, download only one media file
#the 'results.txt' file has two columns: name(0) and link with media url(1)

import time #manipulating dates and times
import requests
from os.path import isfile #checking if file of a given directory exists

filename = '/Users/rembeza/Desktop/MyProject/results4.txt'
#change pathway or result file name if necessary


file = open(filename, "r")

for line in file:
    fields = line.split("\t")
    
    
    Medium = fields[0].rstrip()
    Name = 'Medium' + Medium.strip('http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_')
    
    url = Medium
    
    
    filename = '/Users/rembeza/Desktop/DSMZ_Media_pdfs/' + Name
    #saving the pdf with medium as a file name
    
    if isfile(filename) is False:
        result = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(result.content)
        time.sleep(1) # script waits 1 sec before downloading another link
        
          

file.close()
