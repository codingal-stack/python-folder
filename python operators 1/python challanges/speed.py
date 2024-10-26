c1 = 10
c2 = 20
c3 = 30
avg = c1 + c2 + c3/3
if avg > c1:
    print("c1 is slowest")
elif avg > c2:
    print("c2 and  are slow")
elif avg > c3:
    print("c3 is slowest")
elif avg > c1 and avg > c2:
    print("c1 and c2 are slower")
elif avg > c2 and avg > c3:
    print("c2 and c3 are slower")
elif avg > c3 and avg > c1:
    print("c3 and c1 are slower")
else:
    print("none are slow")
    
