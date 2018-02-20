import math

primes = [2,3]
largestprime = 3

def main():
	test = 80
	pflist = primeFactors(test)
	
	print (pflist)

	

def primeFactors(number):

	factors = []
	global largestprime							# grab our largest generated prime
	# check already generated primes
	while (number > 1):
		for i in primes:
			if (number % i == 0):
				number = number / i
				factors.append (i)
				break
			# end if
		# end for
		# if we made it all the way through, break
		if (i == largestprime):	
			break
		# end if
	# end while
	# check if we need to generate new primes
	if (largestprime < math.sqrt(number)):
		while (largestprime < math.sqrt(number)):
			largestprime += 2
			# check if new largestprime is actually prime
			isprime = True
			for i in primes:
				if (largestprime % i == 0):
					isprime = False
					break
				# end if
			# end for
			# if it's prime, add it to the list
			if (isprime):
				primes.append(largestprime)
				# also check if this is a factor of number
				if (number % largestprime == 0):
					number = number / largestprime
					factors.append (largestprime)
				# end if
			# end if
		# end while
	# end if
	if (number > 1):
		factors.append(number)
	# end if
		
	return (factors)
# end primeFactors
		
		
	
main()


# TIDALWAVE