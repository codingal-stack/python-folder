maths = int(input("enter math marks"))
sci = int(input("enter sci marks"))
lit = int(input("enter lit marks"))
qh = int(input("enter qh marks"))
art = int(input("enter art marks"))
total = maths + sci + lit + qh + art
avg = total/5

if avg>=90 and avg<=100:
    print("grade is a")
elif avg>=80:
    print("your grade is b")
elif avg>=70:
    print("your grade is c")
elif avg >=60:
    print("your grade is d")
else:
    print("study more")
