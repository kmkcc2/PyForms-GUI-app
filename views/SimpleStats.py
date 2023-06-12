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
        self.option_list = ControlCombo('Wybierz kolumne')
        self.option_list.add_item('---', 0)
        headers = data.getHeaders()
        iter = 1
        for head in headers:
            self.option_list.add_item(head, iter)
            iter = iter + 1
        self.option_list.changed_event = self.selection_changed
        if data.choose != '':

            df = data.read()
            self.min_values = df.min().values.tolist()
            self.min_values.insert(0, 'min')

            self.max_values = df.max().values.tolist()
            self.max_values.insert(0, 'max')

            self.std_values = df.std().values.tolist()
            self.std_values.insert(0, 'std')

            self.median_values = df.median().values.tolist()
            self.median_values.insert(0, 'mediana')

            self.mode_values = df.mode().iloc[0].tolist()
            self.mode_values.insert(0, 'mod')

            self._stats = ControlList('Podstawowe wartości statystyczne')
            self._stats.readonly = True
            headers = data.getHeaders()
            headers.insert(0, "Wartości")
            self._stats.horizontal_headers = headers
            self._stats.__add__(self.min_values)
            self._stats.__add__(self.max_values)
            self._stats.__add__(self.std_values)
            self._stats.__add__(self.median_values)
            self._stats.__add__(self.mode_values)

    def selection_changed(self):
        print (self.option_list.current_index)
        self._stats.clear()
        headers = data.getHeaders()
        if self.option_list.current_index != 0:
            self._stats.horizontal_headers = ['Wartosci',headers[self.option_list.current_index - 1]]
            self._stats.__add__([self.min_values[0], self.min_values[self.option_list.current_index]])
            self._stats.__add__([self.max_values[0], self.max_values[self.option_list.current_index]])
            self._stats.__add__([self.std_values[0], self.std_values[self.option_list.current_index]])
            self._stats.__add__([self.median_values[0], self.median_values[self.option_list.current_index]])
            self._stats.__add__([self.mode_values[0], self.mode_values[self.option_list.current_index]])
        else:
            self._stats.horizontal_headers = ['Wartosci', *headers]
            self._stats.__add__(self.min_values)
            self._stats.__add__(self.max_values)
            self._stats.__add__(self.std_values)
            self._stats.__add__(self.median_values)
            self._stats.__add__(self.mode_values)


