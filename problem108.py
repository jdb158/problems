def main():
	number_of_sums = 0
	maxsums = 0
	denominator = 4
	
	while (number_of_sums <=10):
		# reset number of sums
		number_of_sums = 0
		denoms = []
		
		for i in range(2, denominator * 2):
			for subtractant in range (1, denominator):
		
				new_denominator = denominator * i
				new_numerator = i - subtractant
				reduced_new_denominator = new_denominator // new_numerator
				if (new_denominator % new_numerator == 0):
					print('1/%d = 1/%d + 1/%d' % (denominator, new_denominator, reduced_new_denominator))
					number_of_sums += 1
		
		if (number_of_sums > maxsums):
			maxsums = number_of_sums
			print("1/%d had %d forms" % (denominator, number_of_sums))
		
		# increase denominator for next loop
		denominator += 1
	
	print("1/%d had %d forms" % (denominator, number_of_sums))
		
main()