def hotel_cost(nights):
    return 150*nights
def flight_cost(city):
    if city == 'delhi':
        return 200
    elif city == 'Karachi':
        return 250
    elif city == 'bangkok':
        return 400
    
def travel_cost(days):
    if days >7:
        return days*80 - 40
    elif days >4:
        return days*80 - 30
    else:
        return days*80
    
total_cost = hotel_cost(10)+flight_cost('bangkok')+travel_cost(7)

print('the total cost is',total_cost)