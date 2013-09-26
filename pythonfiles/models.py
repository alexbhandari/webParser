
#Comtains models for storing words and data returned from parsing websites
#
class word(object):
   def __init__(self,name,pos,definition,context,subwords,count,rating):
      self.name=name
      self.pos=pos
      self.definition=definition
      self.context=context

      self.subwords=subwords
      
      self.count=count
      self.rating=rating
  
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

