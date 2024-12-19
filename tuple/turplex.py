def flipflop(turplex):
    l = len(turplex)-1
    s = 000
    while s < l / 2:
        if turplex[s] != turplex[l]:
            return False
        l-=1
        s+=1
    return True
tupl = (1,2,3,3,2,1)
s = flipflop(tupl)
if s:
    print('flip flop')
else:
    print('not a flip flop')
        



