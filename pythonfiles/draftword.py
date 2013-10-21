
#Comtains models for storing words and data returned from parsing websites
#
class draftword(object):
   def __init__(self,usage=None,term=None,part_of_speech=None,sense=None,trace=None):
      self.usage=usage
      self.term=term
      self.part_of_speech=part_of_speech
      self.sense=sense
      self.trace=trace

  
   def __str__(self):
      return self.usage
   def get_usage(self):
      return self.usage
   def get_part_of_speech(self):
      return self.part_of_speech
   def get_term(self):
      return self.term
   def get_sense(self):
      return self.sense
   def get_trace(self):
      return self.trace
   
   def set_usage(self,usage):
      self.usage = usage
   def set_part_of_speech(self,pos):
      self.part_of_speech = pos
   def set_term(self,term):
      self.term = term
   def set_sense(self,sense):
      self.contex = contex
   def set_trace(self,trace):
      self.trace=trace
