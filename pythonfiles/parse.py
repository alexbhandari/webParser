#Basic script: get html, extract words, parse, and count
import urllib.request
from bs4 import BeautifulSoup
from collections import Counter
import operator
import re
#get html
with urllib.request.urlopen('http://www.nytimes.com') as url:
   page = url.read()
#beautiful soup object
soup = BeautifulSoup(page)
text = ""
#extract and combine paragraphs
paragraphs = soup.find_all('p')
for x in range (0,len(paragraphs)):
   text = text + paragraphs[x].getText()
#separate all words (returns list)
words = text.split()
#test regex
for x in words:
   y=re.search(r'\.$|\W$',x)
   if y:
      if y.lastgroup is not None:
         for l in range (0,y.lastindex):
            print(y.group(l))
      else:
         print(y.group(0))
#parse words. 
#regex: \.$ is periods at the end of string OR \W$ is special chars at end 
#of string (which also includes special chars alone.
#still need work on apostrophies, missed spaces after periods and word?word
#this should be made into a method.
#words2 = [re.sub(r'\.$','',x) for x in words]
words[:] = [re.sub(r'\.$|\W$','',x) for x in words]
#returns a dictionary object
count = Counter(words)

#switched to dict_items
count_items = count.items()
#switched to list: sorted returns list
sorted_words = list(reversed(sorted(count_items,key=operator.itemgetter(1))))
