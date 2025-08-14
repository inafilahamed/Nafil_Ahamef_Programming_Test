'''Problem-1: Create a small calculator which performs operations such as
Addition, Subtraction, Multiplication and Division using class.'''

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return 'cannot divided by zero!'

a = int(input("Enter first number:"))
b = int(input("enter second number:"))
operation = input("enter operation(+,-,*,/)")

calc = Calculator(a,b)

if operation == '+':
    print('result:',calc.add())
elif operation == '-':
    print('result:',calc.subtract())
elif operation == '*':
    print('result:',calc.multiply())
elif operation == '/':
    print('result:', calc.divide())
else:
    print("Invalid operation")