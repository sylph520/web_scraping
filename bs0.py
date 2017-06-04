# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:15:38 2017

@author: Admin
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
print (html.read())
bsObj = BeautifulSoup(html)

namelist = bsObj.findAll('span',{'class':'green'})
for name in namelist:
    print (name.get_text())

allText = bsObj.findAll(id = 'text')
print (allText[0].get_text())

print (bsObj.findAll("",{'id':'text'})[0].get_text())

bsObj.findAll(class_ = 'green')
bsObj.findAll('',{'class':'green'})

html2 = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj2 = BeautifulSoup(html2)
for child in bsObj2.find("table",{"id":"giftList"}).descendants:
    print(child)
    
