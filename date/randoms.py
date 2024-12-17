import random
import datetime

def datetimer1(start,end):
    random_sec =random.randint(0,int ((end - start).total_seconds()))
    rd = datetime.timedelta(seconds = random_sec)
    return start + rd
    
start = datetime.datetime(2020,1,1)
end = datetime.datetime(2021,1,1)
r = datetimer1(start,end)
print(r.date())