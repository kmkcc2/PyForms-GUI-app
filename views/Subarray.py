from pyforms.basewidget import (
    BaseWidget
)
from pyforms.controls   import (
    ControlButton,
    ControlLabel,
    ControlText,
    ControlList,
    )
import settings
from analisys import data
from views.FileChoose import FileChoose
import re
import pandas as pd
import csv
import os

class Subarray(BaseWidget):

   #Definition of the forms fields
    def __init__(self):
        super().__init__('Wybierz wiersze do zapisu')

        self.setGeometry(660,300,650,500)
        self.set_margin(10)
        self.set_margin(10)
        self.setContentsMargins(10, 10, 10, 10)

        self._info = ControlLabel("Prosze podać przedziały oddzielone przecinkami np. 1-5,10-15")
        self._row_index = ControlText("Numery wierszy")
        self._info_col = ControlLabel("Dostępne kolumny: row age sex cp trestbps chol fbs restecg thalach exang oldpeak slope ca thal num")
        self._col_index = ControlText("Nazwy column")

        d = self.load_data()
        if data.choose != '':
            self._stats = ControlList(data.choose.split('.')[1])
            self._stats.readonly = True
            headers = []
            for col in d.columns:
                headers.append(col)
            self._stats.horizontal_headers = headers
            for index, row in d.iterrows():
                self._stats.__add__(row)
        self._show_button = ControlButton("Podgląd podtabeli")
        self._show_button.value = self.preview
        self._save_subarray = ControlButton("Zapisz podtabelę")
        self._save_subarray.value = self.save

    def load_data(self):
        d = data.read()
        if not d.columns.__contains__("row"):
            d.insert(0, "row", range(1,len(d.index) + 1))
        return d

    def preview(self):
        text_row = self._row_index.value
        text_arr_row = text_row.split(",")
        text_row_ok = True
        for ran in text_arr_row:
            if(self.use_regex(ran.strip())):
                pass
            else:
                text_row_ok = False
        if not text_row_ok:
            self._row_index.value = "Prosze wybrać poprawne zakresy"

        text_col = self._col_index.value
        text_arr_col = text_col.split(",")
        text_col_ok = True
        picked_headers = []
        for ran in text_arr_col:
            headers = self._stats._horizontalHeaders
            if(headers.__contains__(ran.strip())):
                picked_headers.append(ran.strip())
            else:
                text_col_ok = False
        if not text_col_ok:
            self._col_index.value = "Prosze wybrać poprawne zakresy"

        if text_col_ok and text_row_ok:
            rows_index = []
            for range_row in text_arr_row:
                range_row.strip()
                rows = range_row.split("-")
                rows_index.append(rows)

            df = self.load_data()
            headers_index = []
            for ind in picked_headers:
                headers_index.append(df.columns.get_loc(ind))
            filtered = []
            for set in rows_index:
                left = int(set[0]) - 1
                right = int(set[1])
                filtered.append(df.iloc[left:right, headers_index])
            result = pd.concat(filtered)
            self._stats.clear()

            headers = []
            for col in result.columns:
                headers.append(col)
            self._stats.horizontal_headers = headers

            for index, row in result.iterrows():
                    self._stats.__add__(row)
            filtered = []

    def save(self):
        if os.path.exists(data.save_path + '/dataframe.csv'):
                # Usuwanie pliku
                os.remove(data.save_path + '/dataframe.csv')

        with open(data.getSavePath() + '/dataframe.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self._stats.horizontal_headers)
            for row in self._stats.value:
                writer.writerow(row)
        self.warning("Plik zapisany")

    def use_regex(self, input_text):
        pattern = re.compile("[0-9]+-[0-9]+$", re.IGNORECASE)
        return pattern.match(input_text)