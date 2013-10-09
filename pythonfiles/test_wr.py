from wordreference import word_ref
d = word_ref()
cat = d.query('cat')
draftlist = []
trace = []
word_ref.populate(cat,draftlist,trace)
print(draftlist)
print(trace)
