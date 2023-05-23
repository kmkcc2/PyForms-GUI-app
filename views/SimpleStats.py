from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlButton,
    ControlCombo,
    ControlDir,
    ControlList,
    ControlLabel
    )
import settings
import pandas as pd
from analisys import data
from views.FileChoose import FileChoose


class SimpleStats(BaseWidget):

   #Definition of the forms fields
    def __init__(self):
        super().__init__('Statystyka')
        self.setGeometry(660,300,800,300)
        settings.PYFORMS_STYLESHEET = '../style.css'
        self.set_margin(10)
        self.set_margin(10)
        self.setContentsMargins(10, 10, 10, 10)
        if data.choose != '':

            df = data.read()
            min_values = df.min().values.tolist()
            min_values.insert(0, 'min')

            max_values = df.max().values.tolist()
            max_values.insert(0, 'max')

            std_values = df.std().values.tolist()
            std_values.insert(0, 'std')

            median_values = df.median().values.tolist()
            median_values.insert(0, 'mediana')

            mode_values = df.mode().iloc[0].tolist()
            mode_values.insert(0, 'mod')

            self._stats = ControlList('Podstawowe wartości statystyczne')
            self._stats.readonly = True
            headers = data.getHeaders()
            headers.insert(0, "Wartości")
            self._stats.horizontal_headers = headers
            self._stats.__add__(min_values)
            self._stats.__add__(max_values)
            self._stats.__add__(std_values)
            self._stats.__add__(median_values)
            self._stats.__add__(mode_values)



