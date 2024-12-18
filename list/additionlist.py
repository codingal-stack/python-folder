l = [1,2,3,4,5,6,7,8,9,10]

print(l)



sum = 0
for i in l:
    sum = sum + i
print('sum of list is',sum)

avg = sum / len(l)

print('avg of list is',avg)

#min and max of list

print('min of list is',min(l))
print('max of list is',max(l))