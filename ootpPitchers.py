import math
import pandas as pd

stats = pd.read_csv('C:\\Users\\usssa\\Desktop\\ootp\\data.csv')
stats.drop(columns=stats.columns[0], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[1], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[2], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[18], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[18], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[18], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[18], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[18], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[18], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[18], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[18], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[18], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[18], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[0], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[1], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[1], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[1], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[1], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[1], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[1], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[1], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[1], 
        axis=1, 
        inplace=True)




stats = stats.groupby(["Name"]).sum()



pd.set_option('display.max_rows', None)

# Add a column - OBP (On-Base-Percentage)

pd.options.mode.chained_assignment = None  # default='warn'

stats = stats.round(1)

stats['WAR/9'] = (stats['WAR']) / stats['IP']
stats['ERA'] = (stats['ER'] * 9) / stats['IP'] 
stats['FIP'] = ((stats['HR'] * 13) + (3 * (stats['BB'] + stats['HP'])) - (2* stats['K'])) / stats['IP'] 

stats = stats.sort_values(by=['WAR/9'])


print(stats[stats.IP > 30])