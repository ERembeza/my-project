#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:04:47 2017

@author: rembeza
"""

#aim: to print a text from a pdf file that's under a given URL
#files carry information about cultivation media

import requests #HTTP library 
import io #BytesIO used in place of a file object, downloading as a bytes stream
import PyPDF2 #getting text from a Pdf file
from PyPDF2 import PdfFileReader

# q and r (below) just carry different media files

r = requests.get('http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium9.pdf')
f = io.BytesIO(r.content)
reader = PdfFileReader(f)
contents = reader.getPage(0).extractText()
print(contents)
f.close()

q = requests.get('http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium129.pdf')
f = io.BytesIO(q.content)
readerq = PdfFileReader(f)
contentsq = readerq.getPage(0).extractText()
print(contentsq)
f.close()

#how to represent the components of a medium in a better form?
#some media files seem to be written in a different form than the others, eq. r vs q...