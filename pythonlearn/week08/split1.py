line = 'A lot           of space'
etc = line.split()
print etc

line1 = 'first;second;third'
thing = line1.split()
print thing
print len(thing)


thing = line1.split(';')
print thing
print len(thing)
