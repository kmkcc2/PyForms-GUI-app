from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlButton,
    ControlCombo,
    ControlDir,
    ControlFile,
    )
from pyforms            import settings
from analisys import data
import os

class FileChoose(BaseWidget):
    file_path = ''

   #Definition of the forms fields
    def __init__(self):
        super().__init__('Analiza danych dot. chorób serca ')
        self.set_margin(10)
        self.set_margin(10)
        self.setContentsMargins(10, 10, 10, 10)
        settings.PYFORMS_STYLESHEET = '../style.css'



        # self._file          = ControlCombo('Wybierz plik do analizy:')
        # self._file.add_item('---', '')
        # self._file.add_item('Cleveland', 'data/processed.cleveland.data')
        # self._file.add_item('Węgry', 'data/processed.hungarian.data')
        # self._file.add_item('Szwajcaria', 'data/processed.switzerland.data')
        # self._file.add_item('Kalifornia', 'data/processed.va.data')
        self._file = ControlFile('Wybierz plik z dysku')
        self._runbutton     = ControlButton('Zapisz')
        self._nan = ControlCombo('Zastąp NaN wartością: ')
        self._nan.add_item('domyslnie', 0)
        self._nan.add_item('0', 1)
        self._nan.add_item('średnia kolumny', 2)
        self._nan.add_item('nie zastępuj', 3)

        # #Define the function that will be called when a file is selected
        # self._file.changed_event    = self.__fileSelectionEvent
        #Define the event that will be called when the run button is processed
        self._runbutton.value       = self.__runEvent
        #Define the event called before showing the image in the player

        #Define the organization of the Form Controls
        self._formset = [
            ('_file'),
            ('_nan'),
            ('_runbutton'),

        ]

    def __runEvent(self):
        data.choose = self._file.value
        data.nan_replace = self._nan.current_index
        if data.choose == '':
            self.warning("Proszę wybrać plik do analizy")
        else:
            self.close()

