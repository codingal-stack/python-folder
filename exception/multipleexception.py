try:
    n1 , n2 = eval(input('enter 2 numbers seperated by a comma'))
    print(n1 / n2)
except SyntaxError as ex:
    print(ex)

except ZeroDivisionError as e:
    print(e)


except:
    print('an error occured')
else:
    print('no error occurd')

finally:
    print('end')