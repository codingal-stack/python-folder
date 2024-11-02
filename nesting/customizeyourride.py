#customize your ride
Choice = int(input("enter your choice1(car)2(bike)"))
if Choice == 1:
    Ch = input('enter your ride 1(bmw) 2(Toyota)')
    if Ch == '1':
        print('u selected bmw')
    elif Ch == '2':
        print("you selected toyota")
    else:
        print('wrong choice')
elif Choice == 2:
    Ch = input('enter your ride 1(scooter) 2(Yamaha)')
    if Ch == '1':
        print('u selected scooter')
    elif Ch == '2':
        print("you selected Yamaha")
    else:
        print('wrong choice')
else:
    print("wrong choice")





