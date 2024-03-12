"""
    If num % 3 == 0 
        Fizz
    Else if num % 5 == 0 
        Buzz
    Else If num % 3 == 0 and num % 5 == 0
        FizzBuzz
"""


def alternative1(lastNumber):
    def evaluate(n):
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 5 == 0:
            return "Buzz"
        elif n % 3 == 0:
            return "Fizz"
        else:
            return n

    print("alternative 1")
    for n in range(1, lastNumber + 1):
        print(evaluate(n))


def alternative2(lastNumber):
    print("alternative 2")

    def evaluate(n):
        output = ""
        if n % 3 == 0:
            output += "Fizz"
        if n % 5 == 0:
            output += "Buzz"
        if output == "":
            output = str(n)
        return output

    for n in range(1, lastNumber + 1):
        print(evaluate(n))


class Alternative3:
    output = ""
    lastNumber = 1

    def __init__(self, lastNumber):
        self.lastNumber = lastNumber

    def isDivisible(self, number, multiple):
        return number % multiple == 0

    def updateOutput(self, result):
        self.output += result

    def evaluate(self, n):
        if self.isDivisible(n, 3):
            self.updateOutput("Fizz")
        if self.isDivisible(n, 5):
            self.updateOutput("Buzz")
        if self.output == "":
            self.output = str(n)
        return self.output

    def render(self):
        for n in range(1, self.lastNumber + 1):
            self.output = ""
            print(self.evaluate(n))


def main():
    # alternative1(100)
    # alternative2(100)
    Alternative3(100).render()


main()
