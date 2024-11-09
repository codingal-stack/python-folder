n = int(input('enter a number'))
sum = 0
num = n
while num != 0:
    rem = num %10
    sum = sum + rem**3
    num //= 10
if sum == n:
    print('it is a armstrong no')
else:
    print('it is not a armstrong no')




    