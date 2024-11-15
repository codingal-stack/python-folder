l = int(input('enter lower limits'))
u = int(input('enter upper limits'))

for i in range(l,u+1):
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        print(i)
    