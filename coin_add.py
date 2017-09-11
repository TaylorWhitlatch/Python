coin = 0
keep_going = True
while keep_going == True:

	print "You currently have %d coins." % coin

	print "Would you like another? (y or n)"
	ans = raw_input("> ")
	
	if (ans == "Y" or ans == "y"):
		coin = coin + 1

	else:
		keep_going = False
		print "You have %d coins." % coin

