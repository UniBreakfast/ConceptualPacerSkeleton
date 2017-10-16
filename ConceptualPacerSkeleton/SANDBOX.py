#myVariable = 5
#v = 4
#for v in locals():
#  if id(v) == id("myVariable"):
#    print(v, locals()[v])


Jack = 5
Konnie = 15
Alex = 22
April = 23
Dave = 8
#v = None
#for v in locals():
#    if '__' not in v and 'v' != v: print(v)


print(', '.join([l for l in locals() if '__' not in l]))