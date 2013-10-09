#This is the main handler for web parsing, API queries, and database loading and storing
#Class Structure
#Handler(now parser)
#|  >(list)words
#|  >(list)filtered
#|  >(word_ref)dictionary
#|  !parse(links)
#|  !query()
#|  !store()
#|--word
#|--word_ref
#|--db_managment

import urllib.request
from bs4 import BeautifulSoup
from collections import Counter
from word import word
import operator
import re

class parse(object):

   def __init__(self):
      self.words = {}
      self.filtered = {}
      self.dictionary = word_ref()
   def get_words(self):
      return self.words
   def get_filtered(self):
      return self.filtered

# PARSER METHODS
   
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

   #get words from links, count and store in word list
   def parse(self,links):
      words = []
      for link in links:
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
      words = Counter(words)
      for x,y in words.items():
         #could also use dict defaultset()
         if x in self.words:
            self.words[x].incr_count(y) 
         else:
            self.words[x] = word(x,None,None,None,None,y,None)

   def pprint(self):
      #create list of words sorted in decending order
      sorted_words = list(reversed(sorted(list(self.words.values()), key=lambda x: x.get_count())))
      #create a list of touples (filtered symbol, count) --SHOULD CHANGE TO OBJECT--
      sorted_filtered = list(reversed(sorted(self.filtered.items(),key=operator.itemgetter(1))))
      #prints a list of touples 
      def p_touple_list(l,f):
         i=0
         for k,c in l:
            print(f.format(str(k),c))
            i = i+1
         print('Number of elements is ' + str(i))
      #prints a list of words
      def p_word_list(l,f):
         i=0
         for w in l:
            print(f.format(w.get_name(),w.get_count()))
            i = i+1
         print('Number of elements is ' + str(i))
      
      print('{:<20} {:<20}'.format('Word','Count'))
      print()
      p_word_list(sorted_words,'{:<20} {:5d}')
      print()
      print('{:<20} {:<20}'.format('Filtered','Count'))
      print()
      p_touple_list(sorted_filtered,'{:<20} {:5d}')

# QUERY METHODS
   def query(self):
      def json_get(json_obj,key):
         json_obj['term0']['PrincipalTranslations']['0']['OriginalTerm']['POS']
      for word in self.words:
         json_obj = self.dictionary.query(word.get_name())
         word.set_pos(json_obj['term0']['PrincipalTranslations']['0']['OriginalTerm']['POS'])
         word.set_definition(json_obj['term0']['PrincipalTranslations']['0']['OriginalTerm']['POS'])
         word.set_context(json_obj['term0']['PrincipalTranslations']['0']['OriginalTerm']['POS'])
         word.set_french_name(json_obj['term0']['PrincipalTranslations']['0']['FirstTranslation']['term'])
         word.set_french_definiton(json_obj['term0']['PrincipalTranslations']['0']['FirstTranslation']]['sense'])
         word.set_french_context(json_obj['term0']['PrincipalTranslations']['0']['FirstTranslation']['context'])


name,pos,definition,context,


# DATABASE METHODS
