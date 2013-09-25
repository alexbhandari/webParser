class word(object):
   def __init__(self,name,pos,definition,context):
      self.name=name
      self.pos=pos
      self.definition=definition
      self.context=context
   
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

class db_entry(object):
   def __init__(self,word,count,rating):
      self.word=word
      self.count=count
      self.rating=rating
   def get_word(self):
      return self.word
   def get_count(self):
      return self.count
   def get_rating(self):
      return self.rating
   def get_name(self):
      return self.word.get_name()

