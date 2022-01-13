#imports
import pandas as pd

#read deaths
url_deaths = 'time_series_covid19_deaths_US.csv'
deaths = pd.read_csv(url_deaths)

#initialize variables
count = 0
total = 0
week = 1

#loop through each column and add up deats
for x in range(4,len(deaths.columns)):
    #break after each week
    if count == 7:
        print('Week ',week, ': ',total)
        #reset variables
        week += 1
        total = 0
        count = 0
    #create list of deaths in column
    deathcolumn = deaths[deaths.columns[x]].tolist()
    #loop to total for that week
    for y in range(len(deathcolumn)):
        total += deathcolumn[y]
    count += 1