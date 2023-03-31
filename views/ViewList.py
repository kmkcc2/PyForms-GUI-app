from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlButton,
    ControlCombo,
    ControlDir,
    ControlList,
    )
import settings
from analisys import data
from views.FileChoose import FileChoose


class ViewList(BaseWidget):

   #Definition of the forms fields
    def __init__(self):
        super().__init__('Podgląd pliku')

        settings.PYFORMS_STYLESHEET = './style.css'


        if data.choose != '':
            self._stats = ControlList(data.choose.split('.')[1])
            self._stats.readonly = True
            d = data.read()
            self._stats.horizontal_headers = ['age','sex','cp','trestbps','chol','fbs','restecg',
                                              'thalach','exang','oldpeak','slope','ca','thal','num']
            for index, row in d.iterrows():
                roww = [row['age'], row['sex'],row['cp'], row['trestbps'], row['chol'], row['fbs'],
                         row['restecg'], row['thalach'], row['exang'], row['oldpeak'], row['slope'], row['ca'], row['thal'], row['num']]
                self._stats.__add__(roww)
                # age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,num

