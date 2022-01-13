#imports
import pandas as pd

#create arrays
states = []
deathlist = []

#read deaths
url_deaths = 'time_series_covid19_deaths_US.csv'
deaths = pd.read_csv(url_deaths)

#create column list
deathcolumns = deaths.columns.tolist()

#loop through states to get death totals
for x in range(0,len(deaths.values)):
    total = 0
    states.append(deaths.values[x][1])
    for y in range(len(deaths.values[x])):
        if deathcolumns[y][0] == '4':
            total += deaths.values[x][y]
    deathlist.append(total)

#find deadliest state
max = 0
for x in range(len(states)):
    if deathlist[x] > max:
        max = deathlist[x]
        deadlieststate = states[x]

print('The deadliest state of April 2020 is',deadlieststate,'at a death count of',max)