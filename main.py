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
from views.Subarray import Subarray
from views.Classification import Classification

class Main(BaseWidget):

    def __selectFile(self):
        win = FileChoose()
        win.parent = self
        win.show()
    def __subarray(self):
        if data.choose != '':
            win = Subarray()
            win.parent = self
            win.show()
        else:
            self.warning("Proszę wybrać plik do analizy")
    def __simpleStats(self):
        if data.choose != '':
            win = SimpleStats()
            win.parent = self
            win.show()
        else:
            self.warning("Proszę wybrać plik do analizy")
    def __classification(self):
        if data.choose != '':
            win = Classification()
            win.parent = self
            win.show()
        else:
            self.warning("Proszę wybrać plik do analizy")
    def __corelations(self):
        if data.choose != '':
            win = Corelation()
            win.parent = self
            win.show()
        else:
            self.warning("Proszę wybrać plik do analizy")
    def __graph(self):
        if data.choose != '':
            win = CorelationGraph()
            win.parent = self
            win.show()
        else:
            self.warning("Proszę wybrać plik do analizy")
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
                    {'Klasyfikacja': self.__classification},
                ],
                'Ekstrakcja': [
                    {'Generuj plik csv': self.__subarray},
                ]
            },
        ]


if __name__ == '__main__':

    from pyforms import start_app
    start_app(Main, geometry=(660,300,660,200))