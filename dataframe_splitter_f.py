# split pandas df based on size in memory
import numpy as np
import pandas as pd

def df_splitter(df):
  max_mem_usage = 373*10**6 #*1048576

  df_mem_usage = df.memory_usage(deep=True).sum()

  if df_mem_usage <= max_mem_usage:
    return df

  else:
    #create a list for appedning split dfs
    global df_list
    df_list = []

    #calc full splits of the df
    full_splits = np.floor(df_mem_usage/max_mem_usage)
    print(full_splits)

    #estab limit for iloc
    idx_limit = int(len(df)/full_splits)

    #add full splits to the df_list
    while len(df) > idx_limit:
      #substract idx_limit from 
      df_split = df.iloc[:len(df)-idx_limit]

      #substract idx_limit from df len, remove these rows from org df and add split df to the list 
      df_split = df.iloc[:len(df)-idx_limit]
      df.drop(df.index[:len(df)-idx_limit],inplace=True)
      df_list.append(df_split)
    
    #add left part of org df to the list and remove
    df_list.append(df)
    df = None
    
    return df_list