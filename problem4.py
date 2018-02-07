def main():
    start = 100
    end = 999

    maxpalindrome = 0

    for i in range(start, end+1):
        for j in range (start, end+1):
            testnumber = i * j
            if ((testnumber > maxpalindrome) and isPalindromic(testnumber)):
                maxpalindrome = testnumber

    print(maxpalindrome)

def isPalindromic(testnumber):
    product = str(testnumber)
    length = len(product)//2

    firsthalf = product[:length]
    secondhalf = product[(-1*length):][::-1]    # I looked this up. this is how you reverse a string

    if (firsthalf == secondhalf):
        return True
    return False

main()
