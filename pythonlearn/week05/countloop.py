count = 0
print 'Before',count
for thing in [9,41,12,3,74,15] :
  count = count + 1
  print count,thing
print 'After',count

running_total = 0
print 'Before',running_total
for thing in [9,41,12,3,74,15] :
  running_total = running_total + thing
  print running_total,thing
print 'After',running_total
