# -*- coding: utf-8 -*-
"""code_for_lei.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kPtHOxnDxkTTihi8bgjcyIvZCc36FkXi

Code Snippet Written for My Friend Lei
"""

#import pandas
import pandas as pd

#make sampletable
df = pd.DataFrame({"r1" : [4 ,5, 6], "r2" : [7, 8, 9], "run" : [10, 11, 10]}, index = [1, 2, 3])
df

def sampletable(df):
    df2 = df.groupby('run').apply(lambda x: x['r1'].unique())
    df3 = df.groupby('run').apply(lambda x: x['r2'].unique())
    r1 = df2.values.tolist()
    r2 = df3.values.tolist()
    return r1,r2

sampletable(df)