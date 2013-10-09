
#Comtains models for storing words and data returned from parsing websites
#
class word(object):
   def __init__(self,name=None,part_of_speech=None,definition=None,context=None,subwords=None,count=None,rating=None):
      self.name=name
      self.part_of_speech=part_of_speech
      self.definition=definition
      self.context=context

      self.subwords=subwords
      
      self.count=count
      self.rating=rating
  
   def __str__(self):
      return self.name
   def get_name(self):
      return self.name
   def get_part_of_speech(self):
      return self.part_of_speech
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
   def set_part_of_speech(self,pos):
      self.part_of_speech = pos
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

   def iterset(self
