from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlButton,
    ControlCombo,
    ControlDir,
    ControlList,
    )
from pyforms            import settings
from analisys import data


class FileChoose(BaseWidget):
    file_path = ''
    save_path = ''

   #Definition of the forms fields
    def __init__(self):
        super().__init__('Analiza danych dot. chorób serca 2')

        settings.PYFORMS_STYLESHEET = './style.css'



        self._file          = ControlCombo('Wybierz plik do analizy:')
        self._file.add_item('---', '')
        self._file.add_item('Cleveland', 'data/processed.cleveland.data')
        self._file.add_item('Węgry', 'data/processed.hungarian.data')
        self._file.add_item('Szwajcaria', 'data/processed.switzerland.data')
        self._file.add_item('Kalifornia', 'data/processed.va.data')

        self._outputfile    = ControlDir('Scieżka do zapisu raportu:')
        self._runbutton     = ControlButton('Zapisz')

        # #Define the function that will be called when a file is selected
        # self._file.changed_event    = self.__fileSelectionEvent
        #Define the event that will be called when the run button is processed
        self._runbutton.value       = self.__runEvent
        #Define the event called before showing the image in the player

        #Define the organization of the Form Controls
        self._formset = [
            ('_file'),
            ('_outputfile'),
            ('_runbutton'),

        ]

    def __runEvent(self):
        data.choose = self._file.value
        self.save_path = self._outputfile.value
        if data.choose == '':
            self.warning("Proszę wybrać plik do analizy")
        elif self._outputfile.value == '':
            self.warning("Proszę wybrać folder do zapisu raportów")
        else:
            self.close()
