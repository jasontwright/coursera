fhand = open('mbox-short.txt')
count = 0
for line in fhand :
  line = line.rstrip()
  if not '@uct.ac.za' in line :
    continue
  count = count + 1
  print line
print 'Line Count: ', count
