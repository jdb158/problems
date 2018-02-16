def main():
	number_of_sums = 0
	maxsums = 0
	denominator = 4
	denominator_delta = 1
	denoms = []
	
#	THIS IS VERY SLOW...
#	while (denominator <=80):
	while (maxsums <= 100):			
		# reset number of sums
		number_of_sums = 0
		denoms = []
		
		for i in range(2, denominator + 2):			# iterate factor from 2 to denominator + 1
			for subtract in range(1, (i//2)+1):		# iterate from 1 to i/2
				new_denominator = i * denominator		# calculate new denominator
				numer1 = i - subtract					# split numerator
				numer2 = i - numer1
				#print ("Trying %d/%d =\t%d/%d + %d/%d\tsub: %d\t%s %s" % (i, new_denominator, numer1, new_denominator, numer2, new_denominator, subtract,(new_denominator%numer1==0),(new_denominator%numer2==0)))
				
				if (new_denominator % numer1 == 0 and new_denominator % numer2 == 0):
					reduced_d1 = new_denominator // numer1
					reduced_d2 = new_denominator // numer2
					if (reduced_d1 not in denoms):
						#print ("1/%d = 1/%d + 1/%d" % (denominator, reduced_d1, reduced_d2))
						number_of_sums += 1
						denoms.append(reduced_d1)
						denoms.append(reduced_d2)
		
		
		
		if (number_of_sums > maxsums):
			maxsums = number_of_sums
			print("1/%d had %d forms" % (denominator, number_of_sums))
		
		# increase denominator for next loop
		denominator += denominator_delta
	
	print("1/%d had %d forms" % (denominator-denominator_delta, number_of_sums))
		
main()

# 1/10 	= 2/20 = 1/20 + 1/20							**
		# = 3/30 = 1/30 + 2/30 = 1/30 + 1/15			**
		# = 4/40 = 1/40 + 3/40 xxx
			   # = 2/40 + 2/40 = 1/20 + 1/20	dupe
		# = 5/50 = 1/50 + 4/50 xxx
			   # = 2/50 + 3/50 xxx
		# = 6/60 = 1/60 + 5/60 = 1/60 + 1/12			**
			   # = 2/60 + 4/60 = 1/30 + 1/15	dupe
			   # = 3/60 + 3/60 = 1/20 + 1/20	dupe
		# = 7/70 = 1/70 + 6/70 xxx
			   # = 2/70 + 5/70 = 1/35 + 1/14			xx
			   # = 3/70 + 4/70 xxx
		# = 8/80 = 1/80 + 7/80 xxx
			   # = 2/80 + 6/80 xxx
			   # = 3/80 + 5/80 xxx
			   # = 4/80 + 4/80 = 1/20 + 1/20	dupe
		# = 9/90 = 1/90 + 8/90 xxx
			   # = 2/90 + 7/90 xxx
			   # = 3/90 + 6/90 = 1/30 + 1/15	dupe
			   # = 4/90 + 5/90 xxx
		# = 10/100 = 1/100 + 9/100 xxx
				 # = 2/100 + 8/100 xxx
				 # = 3/100 + 7/100 xxx
				 # = 4/100 + 6/100 xxx
				 # = 5/100 + 5/100 = 1/20 + 1/20	dupe
		# = 11/110 = 1/110 + 10/110= 1/110+ 1/11		**
				 # = 2/110 + 9/110 xxx
				 # = 3/110 + 8/110 xxx
				 # = 4/110 + 7/110 xxx
				 # = 5/110 + 6/110 xxx