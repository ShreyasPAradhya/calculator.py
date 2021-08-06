import sys
from colorama import Fore, Back, Style
while True:
    n=str(input("Enter the operation u want to perform(+ , -, /, %, *)\nelse to exit press 'x'"))
    a=int(input('Enter the first number -'))
    b=int(input('Enter the second number -'))

    if n in ('+','-','/','%','*'):
        if n=='+':
            print(a+b)

            continue
        if n=='-':
            print(a - b)
            continue
        if n=='/':
            print(a / b)
            continue
        if n=='%':
            print(a % b)
            continue
        if n=='*':
            print(a * b)

            continue
    elif n=='x':
        sys.exit(0)
    else:
        print('Please give a valid input')
        continue

