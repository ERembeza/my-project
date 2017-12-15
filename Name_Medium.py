#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:17:34 2017

@author: rembeza
"""

# to extract names of microorganisms and links to their culture media from a file containing various information about 


file = open("DSM_parsed_cleaned_2.txt", "r")
results = open("results.txt", "w")

for line in file:
    fields = line.split("\t")
    
    DTB = fields[0]
    ID = fields[1]
    Name = fields[2]
    Temp = fields[3]
    Risk = fields[4]
    Domain = fields[5]
    TaxId = fields[6]
    Isolation = fields[7]
    Medium = fields[8].rstrip() #strips the white space characters, such as /n /t and other
    #print(repr(Medium)) #printing visual representation, with new lines, etc.
    if Medium != 'None':
        results.write(Name + "\t" + Medium +"\n") #”\n” representation for enter, goes to the next line
results.close()
file.close()
    

    
    
