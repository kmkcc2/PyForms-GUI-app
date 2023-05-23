from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlButton,
    ControlCombo,
    ControlDir,
    ControlList,
    ControlLabel
    )
import settings
from analisys import data
from views.FileChoose import FileChoose


class ViewList(BaseWidget):

   #Definition of the forms fields
    def __init__(self):
        super().__init__('Podgląd pliku')

        self.setGeometry(660,300,650,500)
        self.set_margin(10)
        self.set_margin(10)
        self.setContentsMargins(10, 10, 10, 10)

        if data.choose != '':
            self._stats = ControlList(data.choose.split('.')[1])
            self._stats.readonly = True
            d = data.read()
            self._stats.horizontal_headers = data.getHeaders()
            for index, row in d.iterrows():
                self._stats.__add__(row)
                # age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,num

