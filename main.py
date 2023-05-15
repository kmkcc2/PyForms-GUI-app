from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlButton,
    ControlCombo,
    ControlLabel,
    ControlList,
    )

from pyforms            import settings

import analisys.data as data
from views.FileChoose import FileChoose
from views.SimpleStats import SimpleStats
from views.ViewList import ViewList
from views.Corelations import Corelation
from views.CorelationGraph import CorelationGraph

class Main(BaseWidget):

    def __selectFile(self):
        win = FileChoose()
        win.parent = self
        win.show()


    def __simpleStats(self):
        win = SimpleStats()
        win.parent = self
        win.show()

    def __corelations(self):
        win = Corelation()
        win.parent = self
        win.show()
    def __graph(self):
        win = CorelationGraph()
        win.parent = self
        win.show()
    def __viewFile(self):
        if data.choose != '':
            win = ViewList()
            win.parent = self
            win.show()
        else:
            self.warning("Proszę wybrać plik do analizy")


    def __pastEvent(self):
        ...

    def analyse(self):
        pass



    def __init__(self, *args, **kwargs):
        super().__init__('Analiza danych dot. chorób serca')

        settings.PYFORMS_STYLESHEET = 'style.css'

        self.formset = []
        self.mainmenu = [
            {
                'Plik': [
                    {'Otwórz': self.__selectFile},
                    {'Podgląd': self.__viewFile},
                ],
                'Analiza': [
                    {'Podstawowa statystyka': self.__simpleStats},
                    {'Analiza korelacji': self.__corelations},
                    {'Zależności': self.__graph},
                    {'Klasyfikacja': self.__simpleStats},
                ],
                'Ekstrakcja': [
                    {'Generuj plik csv': self.__simpleStats},
                ]
            },
        ]


if __name__ == '__main__':

    from pyforms import start_app
    start_app(Main, geometry=(660,300,660,200))