import sys
import pandas as pd

def all_recycling_days(year):
    return pd.date_range(start=str(year), end=str(year+1), 
                         freq='W-THU').strftime('%d/%m').tolist()

def all_rubbish_days(year):
    return pd.date_range(start=str(year), end=str(year+1), 
                         freq='W-FRI').strftime('%d/%m').tolist()

year = int(sys.argv[1])
sched = []

for day in all_recycling_days(year):
    sched.append((day, 1))
    
for day in all_rubbish_days(year):
    sched.append((day, 2))

print(sched)