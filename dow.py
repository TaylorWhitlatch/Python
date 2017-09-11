dow = int(raw_input("What day is it today? 0-6 "))
weekdays = ["SUNDAY","MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]


print weekdays[dow]
if dow == 0 or dow == 6:
	print "You get to sleep in!"
else:
	print "You have to work!"
