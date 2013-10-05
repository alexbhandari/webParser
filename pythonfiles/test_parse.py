#from pprint import pprint
import operator
import parse
#link = ['http://www.nytimes.com']
link = ['http://www.nytimes.com']
parse_object = parse.parse(link)
parse_object.parse()

#sort = parse_object.get_words().values()
sorted_words = list(reversed(sorted(list(parse_object.get_words().values()), key=lambda x: x.get_count())))
sorted_filtered = list(reversed(sorted(parse_object.get_filtered().items(),key=operator.itemgetter(1))))

def plist(l,f):
   i=0
   for k,c in l:
      print(f.format(str(k),c))
      i = i+1
   print('Number of elements is ' + str(i))
def pwlist(l,f):
   i=0
   for w in l:
      print(f.format(w.get_name(),w.get_count()))
      i = i+1
   print('Number of elements is ' + str(i))

print('{:<20} {:<20}'.format('Word','Count'))
print()
#pdict(parse_object.get_words(),'{:<20} {:<20}')
pwlist(sorted_words,'{:<20} {:5d}')
print()
print('{:<20} {:<20}'.format('Filtered','Count'))
#pdict(parse_object.get_filtered(),'{:<20} {:<20}')
plist(sorted_filtered,'{:<20} {:5d}')


#pprint(parse_object.get_words())
#pprint(parse_object.get_filtered())
