def add(a,b):
    return  a+b
def sub(a,b):
    return  a-b
def mul(a,b):
    return  a*b
def div(a,b):
    return  a/b


op = input('choose your choice\n1.)addition\n2.)substraction\n3.)muiltiplication\n4.division')
if op == '1':
    a = int(input('enter first number'))
    b = int(input("enter second number"))
    print('addition of 2 numbers is',add(a,b))
elif op == '2':
    a = int(input('enter first number'))
    b = int(input("enter second number"))
    print('substraction of 2 numbers is',sub(a,b))
elif op == '3':
    a = int(input('enter first number'))
    b = int(input("enter second number"))
    print('multiplycation of 2 numbers is',mul(a,b))
elif op == '4':
    a = int(input('enter first number'))
    b = int(input("enter second number"))
    print('division of 2 numbers is',div(a,b))

3