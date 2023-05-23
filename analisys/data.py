import pandas as pd
choose = 'data/processed.cleveland.data' # docelowo pusty string
save_path = 'data/'

def read():
    if choose != '':
        data =  pd.read_csv(choose, sep=",", header=0, na_values='?')
        return data
def getSavePath():
    return save_path
def getHeaders():
    df = read()
    headers = []
    for col in df.columns:
        headers.append(col)
    return headers