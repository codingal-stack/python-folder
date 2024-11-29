def factorial(n):
    '''This is a code about factorial'''
    if n == 0:
        return 1 
    else:
        return factorial(n - 1)*n
print(factorial.__doc__)
print('the factorial of the number is',factorial(20))