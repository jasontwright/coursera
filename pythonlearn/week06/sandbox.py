fruit = 'banana'
letter = fruit[1]
print letter

n = 3
w = fruit[n - 1]
print w

print len(fruit)

index = 0
while index < len(fruit) :
  letter = fruit[index]
  print index,letter
  index = index + 1

for letter in fruit :
  print letter

word = 'banana'
count = 0
for letter in word :
  if letter == 'a' :
    count = count + 1
print count

if 'nan' in word :
  print 'Found it!'

line = 'Please have a nice day'
if line.startswith('Please') :
  print "Yes!"

if line.startswith('p') :
  print "Yes!"

print len('banana') * 7

greet = 'Hello Bob'
print greet.upper()

data = 'From stephen.marquard@uct.ac.za Sat Jan'
pos = data.find('.')
print data[pos:pos+3]
