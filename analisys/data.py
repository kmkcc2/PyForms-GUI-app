import pandas as pd
import random
import numpy as np
choose = 'data/processed.cleveland.data' # docelowo pusty string
nan_replace = '0'

def read():
    if choose != '':
        data =  pd.read_csv(choose, sep=",", header=0, na_values='?')
        if nan_replace == 1:
            data = data.fillna(0)
        elif nan_replace == 2:
            data = data.fillna(data.mean())
        elif nan_replace == 0:
            for col in data:
                data[col] = data[col].fillna(int(round(data[col].mean())))
        return data
def getHeaders():
    df = read()
    headers = []
    for col in df.columns:
        headers.append(col)
    return headers