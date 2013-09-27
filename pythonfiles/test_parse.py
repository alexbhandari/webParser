from pprint import pprint
import operator
import parse
link = ['http://www.nytimes.com']
parse_object = parse.parse(link)
parse_object.parse()

sorted_words = list(reversed(sorted(parse_object.get_words().items(),key=operator.itemgetter(1))))
sorted_filtered = list(reversed(sorted(parse_object.get_filtered().items(),key=operator.itemgetter(1))))

def plist(d,f):
   for i,c in d:
      print(f.format(str(i),str(c)))

print('{:<20} {:<20}'.format('Word','Count'))
#pdict(parse_object.get_words(),'{:<20} {:<20}')
plist(sorted_words,'{:<20} {:<20}')
print()
print('{:<20} {:<20}'.format('Filtered','Count'))
#pdict(parse_object.get_filtered(),'{:<20} {:<20}')
plist(sorted_filtered,'{:<20} {:<20}')


#pprint(parse_object.get_words())
#pprint(parse_object.get_filtered())
