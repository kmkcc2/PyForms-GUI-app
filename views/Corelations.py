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
        self.option_list_x = ControlCombo('Wybierz kolumne')
        self.option_list_x.add_item('---', 0)
        headers = data.getHeaders()
        iter = 1
        for head in headers:
            self.option_list_x.add_item(head, iter)
            iter = iter + 1
        self.option_list_x.changed_event = self.selection_changed

        self.option_list_y = ControlCombo('Wybierz kolumne')
        self.option_list_y.add_item('---', 0)
        headers = data.getHeaders()
        iter = 1
        for head in headers:
            self.option_list_y.add_item(head, iter)
            iter = iter + 1
        self.option_list_y.changed_event = self.selection_changed
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

    def selection_changed(self):
        headers = data.getHeaders()
        if self.option_list_x.current_index != 0 and self.option_list_y.current_index != 0:
            self._stats.clear()
            header_x = headers[self.option_list_x.current_index - 1]
            header_y = headers[self.option_list_y.current_index - 1]
            iter = 0
            headers_to_drop = []
            for x in headers:
                if x != header_x and x != header_y:
                    headers_to_drop.append(x)
                iter = iter + 1
            new_df = data.read().drop(headers_to_drop, axis = 1)
            corr_matrix = new_df.corr()
            matrix_headers = corr_matrix.columns.tolist()
            corr_matrix_with_headers = [matrix_headers] + corr_matrix.values.tolist()
            for row in corr_matrix_with_headers:
                row.insert(0, matrix_headers[corr_matrix_with_headers.index(row)])
            self._stats.value = corr_matrix_with_headers
        else:
            headers = data.getHeaders()
            iter = 1
            for head in headers:
                self.option_list_y.add_item(head, iter)
                iter = iter + 1
            self.option_list_y.changed_event = self.selection_changed
            df = data.read()
            corr_matrix = df.corr()
            # print(corr_matrix)
            headers = corr_matrix.columns.tolist()
            corr_matrix_with_headers = [headers] + corr_matrix.values.tolist()
            for row in corr_matrix_with_headers:
                row.insert(0, headers[corr_matrix_with_headers.index(row)])
            self._stats.value = corr_matrix_with_headers