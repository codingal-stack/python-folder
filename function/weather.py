def weathercondition(w):
    if w == 'Autumn':
        print('The weather is good')
    elif w == 'Spring':
        print('The weather is excellent')
    elif w == 'Winter':
        print('its very cold')
    elif w == 'summer':
        print('its too hot')
    else:
        print('weather not recognized')
        
s = input('enter the season')

weathercondition(s)