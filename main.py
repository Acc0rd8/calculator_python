def add(num1, num2):
    return f'\n\n{num1} + {num2} = {num1 + num2}\n\n'

def sub(num1, num2):
    return f'\n\n{num1} - {num2} = {num1 - num2}\n\n'

def mul(num1, num2):
    return f'\n\n{num1} * {num2} = {num1 * num2}\n\n'

def div(num1, num2):
    try:
        return f'\n\n{num1} / {num2} = {num1 / num2}\n\n'
    except ZeroDivisionError:
        return f'\nDivided by zero\nBruh...........\n\n'

def menu():
    print('1. Add (number1 + number2)\n2. Substract (number1 - number2)\n3. Multiply (number1 * number2)\n4. Divide (number1 / number2)\n\n', end='')

def main():
    menu()
    number = int(input('Choose the correct number: '))
    
    
    if number == 1:
        number1 = int(input('Enter the first number: '))
        number2 = int(input('Enter the second number: '))
        print(add(number1, number2))
        
    elif number == 2:
        number1 = int(input('Enter the first number: '))
        number2 = int(input('Enter the second number: '))
        print(sub(number1, number2))
        
    elif number == 3:
        number1 = int(input('Enter the first number: '))
        number2 = int(input('Enter the second number: '))
        print(mul(number1, number2))
        
    elif number == 4:
        number1 = int(input('Enter the first number: '))
        number2 = int(input('Enter the second number: '))
        print(div(number1, number2))
        
    else:
        print('You entered an incorrect number. Try again...')
        

print('Hello, this is a calculator!\n')
print('Lets start!\n||\n\\/')

while True:
    main()
    
    answer = input('Would you like to continue? ("yes" or "no"): ')
    if answer == 'no':
        break
    else:
        print('\nOK, lets continue\n\n')

print('OK, Good Luck!')