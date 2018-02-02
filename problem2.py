fib1 = 1
fib2 = 1
total = 0

while True:
	fibtemp = fib2
	fib2 = fib1 + fib2
	fib1 = fibtemp
	
	if (fib2 > 4e+6):
		break
	
	if (fib2 % 2 == 0):
		total += fib2

print (total)