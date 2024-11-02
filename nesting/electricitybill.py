unit = int(input("Enter amount of units used"))
if unit < 50:
    amt = unit * 2.60 + 25
elif unit < 100:
    amt = 50 * 2.60 + (unit - 50) * 3.25 + 35
elif unit < 200:
     amt = 50 * 2.60 + (unit - 50) * 5.26 + 45 + 50 * 3.25
else:
    amt = 50 * 2.60 + (unit - 100) * 7.25 + 75 + 50* 3.25  + 100 * 5.26
print('the amount is',amt)
     
    