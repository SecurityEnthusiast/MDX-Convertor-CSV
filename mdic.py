#!/bin/python
# -*- coding: utf-8 -*-

from readmdict import MDX#or MDD  #You need to install lzo Library for gcc and python-lzo,readmdict,ripemd128 and pureSalsa20 Library for python
import csv
import re

csvaddress='XXXX.csv' #Your CSV file name to export

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

mdx= MDX('XXXX.mdx') #Open the original MDX Dictionary file
items = mdx.items()
tx=mdx.items().next() #To fetch first line in your mdx file - If delete this line you miss first line
lst=[]

for counter in items:
    try:
        templst=list(tx)
        templst[1] = remove_html_tags(templst[1])
        lst.append(templst)
        tx=items.next()
    except:
        with open(csvaddress,'w') as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(lst)
