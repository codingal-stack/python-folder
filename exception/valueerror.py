try:
    n = int(input('enter a number'))
    print(n)
except ValueError as ex:
    print('the error is ',ex)
