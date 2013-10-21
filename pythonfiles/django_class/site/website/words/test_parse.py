from words.parse import parse

class ptest:

   parse = parse()

   def test(self):
      list_of_links = []
      list_of_links.append('http://www.nytimes.com')
#      list_of_links.append('file:///home/alexbhandariyoung/effective_django/effectivedjango.com/index.html')
      self.parse.parse(list_of_links,save=False)
      print('parse complete')
      self.parse.query()
      print('query complete')

