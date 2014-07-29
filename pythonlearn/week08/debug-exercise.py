fhand = open('mbox-short.txt')
count = 0
for line in fhand :
  line = line.rstrip()
  words = line.split()
  if words == [] : continue
  if words[0] != 'From' : continue
  count = count + 1
  print words[2]
print 'Total days:',count
