from pprint import pprint
import parse
link = ['http://www.nytimes.com']
parse_object = parse.parse(link)
parse_object.parse()
print('WORDS:')
pprint(parse_object.get_words())
print('Filtered:')
pprint(parse_object.get_filtered())
