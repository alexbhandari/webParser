from pprint import pprint
import parse
link = ['http://www.nytimes.com']
parse_object = parse.parse(link)
parse_object.parse()

def pdict(d,f):
   for i,c in d.items():
      print(f.format(str(i),str(c)))

print('{:<20} {:<20}'.format('Word','Count'))
pdict(parse_object.get_words(),'{:<20} {:<20}')
print()
print('{:<20} {:<20}'.format('Filtered','Count'))
pdict(parse_object.get_filtered(),'{:<20} {:<20}')


#pprint(parse_object.get_words())
#pprint(parse_object.get_filtered())
