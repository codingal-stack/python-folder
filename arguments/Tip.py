def bill(amt,tip):
    total = amt + amt*tip/100
    print(f'total amount is {total}')

amt = float(input('enter the amount'))
bill (amt , 2)
