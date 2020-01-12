import pandas as pd
import numpy as np


def iqr_outliner(arr):
    per_75 = np.nanpercentile(arr,75)
    per_25 = np.nanpercentile(arr,25)
    iqr = per_75 - per_25
    upper_bound = per_75 + (1.5*iqr)
    lower_bound = per_25 - (1.5*iqr)
    return([i for i in arr if i > upper_bound or i<lower_bound])


def basic_exploration(df):
#shape
#info
#null values
#outlinersy

    print(f"Shape of df = {df.shape}")
    print(f"Info = {df.info()}")
    print(df.describe())
    null_df = pd.DataFrame(df.isnull().sum())
    null_df.columns = ["counts"]
    null_df = null_df[null_df["counts"]>0]
    print(null_df)
    num_df = df.select_dtypes(exclude=object)
    dic = {}
    for col in num_df.columns:
        per_75 = np.nanpercentile(df[col],75)
        per_25 = np.nanpercentile(df[col],25)
        iqr = per_75 - per_25
        upper_bound = per_75 + (1.5*iqr)
        lower_bound = per_25 - (1.5*iqr)
        out_liers = [i for i in df[col] if i>upper_bound or i<lower_bound]
        dic[col] = out_liers
    print(f"outliner = {dic}")



    
if __name__ == '__main__':
    df = pd.read_csv("titanic.csv")
    print(basic_exploration(df))    