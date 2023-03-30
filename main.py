from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlButton,
    ControlCombo,
    ControlDir
    )

from pyforms            import settings
import data
class FileAnalysis(BaseWidget):
    def __openEvent(self):
        ...

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
            { 'File': [
                    {'Open': self.__openEvent},
                    '-',
                    {'Save': self.__saveEvent},
                ]
            },
            { 'Edit': [
                    {'Copy': self.__editEvent},
                    {'Past': self.__pastEvent}
                ]
            }
        ]


        #Definition of the forms fields
        self._file          = ControlCombo('Wybierz plik do analizy:')
        self._file.add_item('Cleveland', 'cl')
        self._file.add_item('Węgry', 'hu')
        self._file.add_item('Szwajcaria', 'sw')
        self._file.add_item('Kalifornia', 'ca')

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
        """
        When the file_file is selected instanciate the video in the player
        """
        data.read(self._file.value)

    def __runEvent(self):
        print("run")


if __name__ == '__main__':

    from pyforms import start_app
    start_app(FileAnalysis)