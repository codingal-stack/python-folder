mc = input("do you have a medical cause?")
if mc  ==  'n':
    att = int(input("enter percentage of attendance"))
    if att > 75:
        print("you are eligible for test")
    else:
        print("you are not elgible")
elif mc == 'y':
    print("you are eligble  for test ")

    