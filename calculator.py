def add(x,y):
    return x + y

def factorial(x):
    if x==1 or x==0:
        return 1
    else:
        return x*factorial(x-1)



def subtract(x,y):
    return x - y

def multiply(x,y):
     return x * y

def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        print('number cannot be zero!!')


while True:

    chose=input('''

    what do you want to do?
    1.add
    2.subtracts 
    3.multiply
    4.divide
    5.factorial

    ''')
    if chose=='5':
        num1=int(input('number1: '))
    
    else:
        num1=float(input('number1: '))
        num2=float(input('number2: '))

    if chose == '1':
        print(add(num1,num2))
    elif chose == '2':
        print(subtract(num1,num2))
    elif chose == '3':
        print(multiply(num1,num2))
    elif chose == '4':
        print(divide(num1,num2))
    elif chose =='5':
        print(factorial(num1))

    else:
        print('invalid input')
