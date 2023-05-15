import pandas as pd
choose = 'data/processed.cleveland.data' # docelowo pusty string

def read():
    if choose != '':
        data =  pd.read_csv(choose, sep=",", header=0, na_values='?')
        return data

def getHeaders():
    return ['age','sex','cp','trestbps','chol','fbs','restecg',
                                              'thalach','exang','oldpeak','slope','ca','thal','num']