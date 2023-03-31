import pandas as pd
choose = ''

def read():
    if choose != '':
        data =  pd.read_csv(choose, sep=",", header=0)
        return data

def min(data, column):
    pass

def max(data, column):
    pass

def mediana(data, column):
    pass

def std(data, column):
    pass

def moda(data, column):
    pass