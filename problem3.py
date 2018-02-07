import math

number = 600851475143
rootnum = math.sqrt(number)
primes = [2]
factors = []

currentprime = 2

while (currentprime <= rootnum):

#    DEBUG:
#    print("Number = %d" % number)
#    print("Current Prime = %d" % currentprime)
    
    # check if the number is divisible by the current prime
    if (number % currentprime == 0):
        # if so, do the division and add to the list of prime factors
        number = number / currentprime
        factors.append (currentprime)
    else:
        # if not, find the next prime
        while True:
            currentprime += 1
            isprime = True
            for i in primes:
                if (currentprime % i == 0):
                    isprime = False
                    break
            if (isprime == True):
                break

print(factors)


print(rootnum)
