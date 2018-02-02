total = 0
for x in list(range(1000)):			# create a list with all numbers 0-999 and step through it
	if (x%3 == 0 or x%5 == 0):		# if the value is divisible by 3 or 5
		total += x					# add it to the total

print (total)						# print out the total
