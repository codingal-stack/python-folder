n = input('enter a number')
print(n)
str1 = str(n)
length = len (str1)
if length%2 == 0:
    mid = int(length/2)-1
else:
    mid = int(length/2)

midproduct = int(str1[mid])*int(str1[mid+1])                      
print('mid product is',midproduct)


