#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
email = dict()
for text in handle :
  if not text.startswith('From ') : continue
  words = text.split()
  if words is 0 : continue
  email[words[1]] = email.get(words[1],0) + 1

bigcount = None
bigword = None
for word in email.items() :
  if bigcount is None or email[words[1]] > bigcount :
    bigword = words[1]
    bigcount = email[words[1]]
    print bigword,bigcount
