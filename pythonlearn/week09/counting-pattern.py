counts = dict()
print 'Enter a line of text:'
line = raw_input('')
if len(line) < 1 : line = "the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car"

words = line.split()
print 'Words:',words

print 'Counting...'
for word in words:
  counts[word] = counts.get(word,0) + 1

print 'Counts',counts

print counts.keys()
print counts.values()
print counts.items()

for key,value in counts.items() :
  print key,value
