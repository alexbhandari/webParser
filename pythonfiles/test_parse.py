from parse import parse #get parse class
#link = ['http://www.nytimes.com']
links = []
links.append('http://www.telegraph.co.uk/news/worldnews/africaandindianocean/somalia/10358587/US-Navy-Seals-targeted-senior-al-Shabaab-commander-in-Somalia-raid.html')
#link.append('http://www.nytimes.com/2013/10/06/us/politics/in-surprise-announcement-hagel-recalls-most-defense-department-workers.html')
links.append('http://www.torontosun.com/2013/10/06/vogt-plays-hero-as-as-pull-even-with-tigers')
links.append('http://www.cnn.com/2013/10/06/showbiz/celebrity-news-gossip/miley-cyrus-snl/')
links.append('http://www.theprovince.com/sports/Shot+happy+Canucks+make+look+simple/9003401/story.html')
handler = parse()
handler.parse(links)
handler.pprint()
#handler.query()
