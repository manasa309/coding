def add(x: int, y: int):
    return x+y

def sub(x: int, y: int):
    return x-y

def mul(x: int, y: int):
    if not isinstance(y, (int,float)) or not isinstance(x,(int,float)):
        print('ERROR: Y is not an integer, enter a valid input...')
    elif y == 0 or x==0:
        print('ERROR: multiplication with zero, enter valid input...')
    else:
     return x*y

def div(x:int, y:int):
    if not isinstance(y, int):
        print('ERROR: Y is not an integer, enter a valid input...')
    elif y == 0:
        print('ERROR: division by zero, enter valid input...')
    else:
        return x/y


print('SIMPLE CALCI')
x= float(input('ENTER NUMBER 1:'))
y= float(input('ENTER NUMBER 2:'))
