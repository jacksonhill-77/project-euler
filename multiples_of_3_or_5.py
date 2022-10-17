"""

get an input: 
the number n that we need to go up to (999)
loop through all the numbers n

create a list
test: 
is this number divisible by 3?
if yes, add it to a list
is this number divisible by 5? 
if yes, add it to a list

add the contents of the list 

"""

class Answer:
    def __init__(self):
        self.listOfNumbers = []
        self.summedNumbers = 0

        def askAmountOfNumbers():
            amountOfNumbers = input("How many numbers would you like to go up to?")
            return amountOfNumbers

        def stringToNumber(string):
            number = int(string())
            return number

        def isDivisibleByThreeOrFive(number):
            if number % 3 == 0:
                 return True
            if number % 5 == 0:
                return True

        def findCorrectNumbers():
            amountOfNumbers = stringToNumber(askAmountOfNumbers)
            correctNumbers = []
            for i in range(amountOfNumbers):
                if isDivisibleByThreeOrFive(i):
                    correctNumbers.append(i)
            return correctNumbers

        def sumListContents():
            return sum(findCorrectNumbers())
            
        def runTest():
            return sumListContents()


        self.runTest = runTest()

x = Answer()
print(x.runTest)






