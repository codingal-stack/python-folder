#sum of natural numbers using while loop
n = int(input('enter a number'))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
print('\n sum = ',sum)