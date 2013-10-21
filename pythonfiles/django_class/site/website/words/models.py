#For storing words

from django.db import models

class Word(models.Model):

   name              = models.CharField(max_length=255)
   pos               = models.CharField(max_length=255)
   definition        = models.CharField(max_length=255) 
   context           = models.CharField(max_length=255)
   count             = models.IntegerField ()
   rating            = models.IntegerField ()
   french_name       = models.CharField(max_length=255) 
   french_definition = models.CharField(max_length=255) 
   french_context    = models.CharField(max_length=255) 


   def create( self,name=None,pos='',definition='',context='',
                 count=0,rating=0,
                 french_name='',french_definition='',french_context='' ):
      self.name=name
      self.pos=pos
      self.definition=definition
      self.context=context
      self.count=count
      self.rating=rating
      self.french_name=french_name
      self.french_definition=french_definition
      self.french_context=french_context

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
      self.context = context
   def set_forms(self,forms):
      self.forms = forms
   def set_count(self,value):
      self.count = value
   def set_french_name(self,value):
      self.french_name = value
   def set_french_definition(self,value):
      self.french_definition = value
   def set_french_context(self,value):
      self.french_context = value
   def incr_count(self,value):
      self.count += value
   def compute_rating(self):
      self.rating = count
