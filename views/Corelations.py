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
import os

class Corelation(BaseWidget):

    def __init__(self):
        super(Corelation, self).__init__('Statystyka')
        self.setGeometry(660,300,1000,500)
        self.set_margin(10)
        self.set_margin(10)
        self.setContentsMargins(10, 10, 10, 10)
        # current_dir = os.getcwd()
        # parent_dir = os.path.dirname(current_dir)
        # style_path = os.path.join(parent_dir, 'proj_inf_2023/style.css')
        # print(style_path)

        # settings.PYFORMS_STYLESHEET = style_path

        df = data.read()
        corr_matrix = df.corr()
        # print(corr_matrix)
        headers = corr_matrix.columns.tolist()
        corr_matrix_with_headers = [headers] + corr_matrix.values.tolist()
        for row in corr_matrix_with_headers:
            row.insert(0, headers[corr_matrix_with_headers.index(row)])

        self._stats = ControlList('Macierz korelacji')
        self._stats.readonly = True
        self._stats.value = corr_matrix_with_headers
