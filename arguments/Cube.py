def Cube(number):
    return number*number*number

def divide3(number):
    if number% 3 == 0:
        return Cube (number)
    else:
        return False
    
n = int(input('enter a number'))
print(divide3(n))