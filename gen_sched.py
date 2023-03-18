import sys
import pandas as pd

def allRecyclingDays(year):
    return pd.date_range(start=str(year), end=str(year+1), 
                         freq='W-THU').strftime('%d/%m').tolist()

def allRubbishDays(year):
    return pd.date_range(start=str(year), end=str(year+1), 
                         freq='W-FRI').strftime('%d/%m').tolist()

year = int(sys.argv[1])
sched = []

for day in allRecyclingDays(year):
    sched.append((day, 1))
    
for day in allRubbishDays(year):
    sched.append((day, 2))

print(sched)