from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlButton,
    ControlCombo,
    ControlDir,
    ControlList,
    )

from pyforms            import settings
import data
from views.FileChoose import FileChoose


class FileAnalysis(BaseWidget):
    def __simpleStats(self):
        # if self._file.value == '':
        #     self.warning("Proszę wybrać plik do analizy")
        # elif self._outputfile.value == '':
        #     self.warning("Proszę wybrać folder do zapisu raportów")
        # #else:
        win = FileChoose()
        win.parent = self
        win.show()
        print('w')


    def __saveEvent(self):
        ...

    def __editEvent(self):
        ...

    def __pastEvent(self):
        ...

    def __init__(self, *args, **kwargs):
        super().__init__('Analiza danych dot. chorób serca')

        settings.PYFORMS_STYLESHEET = 'style.css'

        self.mainmenu = [
            { 'Analiza': [
                    {'Wyznacz miary statystyczne': self.__simpleStats},
                    '-',
                    {'Save': self.__saveEvent},
                ]
            },
            { 'Raport': [
                    {'Copy': self.__editEvent},
                    {'Past': self.__pastEvent}
                ]
            }
        ]

        self._file          = ControlCombo('Wybierz plik do analizy:')
        self._file.add_item('---', '')
        self._file.add_item('Cleveland', 'data/processed.cleveland.data')
        self._file.add_item('Węgry', 'data/processed.hungarian.data')
        self._file.add_item('Szwajcaria', 'data/processed.switzerland.data')
        self._file.add_item('Kalifornia', 'data/processed.va.data')

        self._outputfile    = ControlDir('Scieżka do zapisu raportu:')
        self._runbutton     = ControlButton('Run')

        #Define the function that will be called when a file is selected
        self._file.changed_event    = self.__fileSelectionEvent
        #Define the event that will be called when the run button is processed
        self._runbutton.value       = self.__runEvent
        #Define the event called before showing the image in the player

        #Define the organization of the Form Controls
        self._formset = [
            ('_file'),
            ('_outputfile'),
            ('_runbutton'),

        ]


    def __fileSelectionEvent(self):
        if self._file.value != '':
            data.read(self._file.value)

    def __runEvent(self):
        print("run")


if __name__ == '__main__':

    from pyforms import start_app
    start_app(FileAnalysis, geometry=(660,300,660,200))