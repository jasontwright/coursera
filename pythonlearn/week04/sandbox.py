def hello():
  print 'Hello'
  print 'Jason'

def print_lyrics():
  print "I'm a lumberjack, and I'm okay."
  print "I sleep all night and I work all day."

def greet(lang):
  if lang == 'es':
    return 'Hola'
  elif lang == 'fr':
    return 'Bonjour'
  else:
    return 'Hello'

def addtwo(a,b):
  a = int(a)
  b = int(b)
  added = a + b
  return added

#big = max('Hello world')
#print big
#hello()
#print_lyrics()
#print greet(raw_input("Enter es, fr, or en: ")), "Glenn"
print addtwo(raw_input("Enter a number: "),raw_input("Enter a number: "))
