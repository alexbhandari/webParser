#Basic script: get html, extract words, parse, and count
#NEEDS TO BE MADE INTO AN OBJECT/CLASS STRUCTURE
import urllib.request
from bs4 import BeautifulSoup
from collections import Counter
import operator
import re

class parse(object):

   def __init__(self,links):
      self.links = links
      self.words = {}
      self.filtered = {}
   def get_words(self):
      return self.words
   def get_filtered(self):
      return self.filtered
#   def print(self)
   
   #outputs strings in words[] list matching input regex
   def test_regex(words,regex):
      filtered = []
      for x in words:
         y=re.search(regex,x)
         if y:
            if y.lastgroup is not None:
               for l in range (0,y.lastindex):
                  filtered.append(y.group(l))
            else:
               filtered.append(y.group(0))
      count = Counter(filtered)
      return count
   #def print_parse(wcount,filtered):
   #   print('Words: ' + wcount)
   #   print('Filtered: ' + filtered)
   
   def parse(self):

      words = []
      for link in self.links:
         #get html
         with urllib.request.urlopen(link) as url:
            page = url.read()
         #beautiful soup object
         soup = BeautifulSoup(page)
         #extract and combine paragraphs
         paragraphs = soup.find_all('p')
         for x in paragraphs:
            #separate all words (returns list)
            words = words + x.getText().split()
         
      #test regex
      regex = r'\.$|\W$'
      self.filtered = parse.test_regex(words,regex)
      #parse words. 
      #regex: \.$ is periods at the end of string OR \W$ is special chars at end 
      #of string (which also includes special chars alone.
      #still need work on apostrophies, missed spaces after periods and word?word
      #leaves empty strings instead of deleting, I think
      #this should be made into a method.
      words[:] = [re.sub(regex,'',x) for x in words]
      #returns a dictionary object
      self.words = Counter(words)
      
      #switched to dict_items
      #count_items = count.items()
      
      #switched to list: sorted returns list
      #sorted_words = list(reversed(sorted(count_items,key=operator.itemgetter(1))))
