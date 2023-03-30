import pandas as pd

def read(filepath):
    data =  pd.read_csv(filepath, sep=",")
    print(data)