def add(a,b):      return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def divide(a,b):   return a/b if b!=0 else 'Error'

op = input('Choose (+, -, *, /): ')
a  = float(input('First number: '))
b  = float(input('Second number: '))
ops = {'+':add, '-':subtract, '*':multiply, '/':divide}
print('Result:', ops[op](a,b) if op in ops else 'Invalid')
