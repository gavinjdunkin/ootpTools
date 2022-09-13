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
stats.drop(columns=stats.columns[19], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[19], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[19], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[19], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[19], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[19], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[19], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[4], 
        axis=1, 
        inplace=True)
stats.drop(columns=stats.columns[4], 
        axis=1, 
        inplace=True)

frames = [stats, pd.read_csv('C:\\Users\\usssa\\Desktop\\ootp\\reportbatters.csv')]
stats = pd.concat(frames)




stats = stats.groupby(["Name"]).sum()



pd.set_option('display.max_rows', None)

# Add a column - OBP (On-Base-Percentage)

pd.options.mode.chained_assignment = None  # default='warn'

stats = stats.round(1)


stats['WAR/100PA'] = stats['WAR'] * 100 / (stats['PA'])


stats = stats.sort_values(['WAR/100PA'])

file_name = 'reportbatters.csv'
print(stats.to_csv(file_name, encoding='utf-8'))