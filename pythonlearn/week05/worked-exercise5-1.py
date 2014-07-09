#Write a program which reads a list of numbers until "done" is entered.  Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, print an error messagea nd skip to the next number.

count = 0
total = 0
while True :
	inp = raw_input('Enter a number: ')
	if inp == 'done' : break
	if len(inp) < 1 : break #Check for empty line
	
	try :
		num = float(inp)
	except : 
		print 'Invalid input'
		continue
	count = count + 1
	total = total + num
	print num, total, count

print 'Average:', total/count