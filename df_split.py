import pandas as pd

dataset = dataset[['player_name','player_kills']]

df1 = dataset.iloc[:20*10**6] 
dataset = dataset.drop(dataset.index[:20*10**6])

df2 = dataset.iloc[:20*10**6]
dataset = dataset.drop(dataset.index[:20*10**6])

df3 = dataset.iloc[:20*10**6]
dataset = dataset.drop(dataset.index[:20*10**6])

dfl_0 = [dataset,df1,df2,df3]
dfl_1 = []

for i in dfl_0:
    #summarize df
    py_player_kills = pd.DataFrame(i.groupby('player_name')['player_kills'].sum())

    
    #remove data from the df
    i = None

    dfl_1.append(py_player_kills)

dataset = pd.DataFrame(pd.concat(dfl_1).groupby('player_name')['player_kills'].sum())
dataset['player_name'] = dataset.index
print(dataset)