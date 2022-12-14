"""
Both 169 and 961 are the square of a prime. 169 is the reverse of 961.

We call a number a reversible prime square if:

It is not a palindrome, and
It is the square of a prime, and
Its reverse is also the square of a prime.
169 and 961 are not palindromes, so both are reversible prime squares.

Find the sum of the first 50 reversible prime squares.
"""

"""
while loop
    initialise reversible prime square count
    if count = 51 
        break
    test for 
        1. if number is palindrome
            if number.reversed == number
        2. if number is the square of a prime
            for i in range(number):
                test if prime
                    if so, is this prime^2 == number?
        3. when reversed, 2. also applies to it
        if all 3 are true:
            increment count 
"""

def isPalindrome(x):
    reversedNumber = ""
    x = str(x)
    for i in range(len(x), 0, -1):
        print(i)
        reversedNumber += x[i-1]
        print(a)
    if reversedNumber == x:
        return True
    else:
        return False

def isWholeNumber(x):
    return x % 1 == 0

def isPrime(x):
    for y in range(len(x)):
        z = x / y
        if z > 1 and isWholeNumber(z) == True:
            return True
        # Needs work

def isPrimeSquare(x):
    for i in range(len(x)):
    # Incomplete

def checkSatisfiesConditions(x):
    if isPalindrome(x) == True and isPrimeSquare(x) == True
        return True
    # Incomplete


def reversiblePrimeSquares(x):
    currentNumber = 0
    reversiblePrimeSquares = []

    while True:
        if len(reversiblePrimeSquares) == 51:
            break
        if checkSatisfiesConditions(x) == True:
            reversiblePrimeSquares.append(x)
    return sum(reversiblePrimeSquares)
        
    
