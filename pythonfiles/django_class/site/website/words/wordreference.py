#construct dictionary = word_ref()
#lookup word json = dictionary.lookup()
from urllib import request
from urllib.parse import quote
from words.draftword import draftword
import json
class word_ref(object):
   def __init__(self,version='0.8',key='602f9',dictionary='enfr'):
      self.version = version
      self.key = key
      self.dict_type = dictionary
   def __str__(self):
      return "version=%s key=%s dictionary=%s" % (version,key,dict_type)
   #querys word-reference for definiton and translation of word
   #returns JSON object
   def query(self,word):
      http = 'http://'
      host_template = 'api.wordreference.com/%s/%s/json/%s/%s' #/v/k/json/d/w
      host = host_template % (self.version,self.key,self.dict_type,word)
      quote_host = quote(host)
      url = http + quote_host
      #response is bytecode
      response = request.urlopen(url)
      encoding = response.headers.get_content_charset()
      decoded_response = response.read().decode(encoding) #convert to string
      obj = json.loads(decoded_response)
      print(json.dumps(obj,indent=2))
      return obj

   #COULD BE A SEPARATE MODULE - JSON HANDLING
   #creates draftword from one-dimensional json_obj
   @staticmethod
   def draft(json_obj,trace):
      if 'usage' in json_obj.keys():
         usage = json_obj['usage']
      else:
         usage=None
      if 'term' in json_obj.keys():
         term = json_obj['term']
      else:
         term=None
      if 'POS' in json_obj.keys():
         pos = json_obj['POS']
      else:
         pos=None
      if 'sense' in json_obj.keys():
         sense = json_obj['sense']
      else:
         sense=None
      return draftword(usage,term,pos,sense,trace)
   
   #recursively iterates json response, populating draftwords
   #stores a trace of every draftword
   @staticmethod
   def populate(json_obj,draftlist,trace):
      if type(json_obj) is not dict:
         return #invalid
      elif type(json_obj[list(json_obj.keys())[0]]) is not dict:
         draftlist.append(word_ref.draft(json_obj,trace))
         trace = []
         return #reached bottom
      else:
         for key in json_obj.keys():
            trace.append(key)
            word_ref.populate(json_obj[key],draftlist,trace)














