#Comtains models for storing words and data returned from parsing websites
#and word_ref queries
class word(object):
   def __init__( self,name=None,pos=None,definition=None,
                 context=None,subwords=None,count=None,rating=None,
                 french_name=None,french_definition=None,french_context=None ):
      self.name=name
      self.pos=pos
      self.definition=definition
      self.context=context
      self.rating=rating
      self.french_name=None
      self.french_definition=None
      self.french_context=None

      self.count=count
  
   def __str__(self):
      return self.name
   def get_name(self):
      return self.name
   def get_pos(self):
      return self.pos
   def get_definition(self):
      return self.definition
   def get_context(self):
      return self.context
   def get_forms(self):
      return self.forms
   def get_count(self):
      return self.count
   def get_rating(self):
      return self.rating

   def set_name(self,name):
      self.name = name
   def set_pos(self,pos):
      self.pos = pos
   def set_definition(self,definition):
      self.defintion = definition
   def set_context(self,context):
      self.contex = contex
   def set_forms(self,forms):
      self.forms = forms
   def set_count(self,value):
      self.count = value
   def incr_count(self,value):
      self.count += value
   def compute_rating(self):
      self.rating = count

#   def iterset(self):
