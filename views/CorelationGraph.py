from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlButton,
    ControlCombo,
    )
from analisys import data
import matplotlib.pyplot as plt

class CorelationGraph(BaseWidget):
    def __init__(self):
        super(CorelationGraph, self).__init__('Statystyka')
        # self.setGeometry(660,300,600,600)
        self.set_margin(10)
        self.set_margin(10)
        self.setContentsMargins(10, 10, 10, 10)
        self._attr1 = ControlCombo('Wybierz atrybut x')
        self._attr1.add_item('---', '')
        for item in data.getHeaders():
            self._attr1.add_item(item, item)

        self._attr2 = ControlCombo('Wybierz atrybut y')
        self._attr2.add_item('---', '')
        for item in data.getHeaders():
            self._attr2.add_item(item, item)

        self._button_corel = ControlButton('Stwórz wykres zależności')
        self._button_corel.value = self.__runEventCorel

        self._button_hist = ControlButton('Stwórz histogram zmiennej x')
        self._button_hist.value = self.__runEventHist

    def __runEventCorel(self):
        df = data.read()
        header_x = self._attr1.value
        header_y = self._attr2.value
        if header_x != '' or header_y != '':
            mean = df.groupby(header_x)[header_y].mean().reset_index()
            x = mean[header_x]
            y = mean[header_y]

            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.set_xlabel(header_x)
            ax.set_ylabel(header_y)
            ax.set_title("Zmiana wartośći " + header_y + " w zależności od "+header_x)
            plt.show()

    def __runEventHist(self):
        df = data.read()
        header_x = self._attr1.value
        if header_x != '':
            hist_data = df[header_x]
            fig, ax = plt.subplots()
            ax.hist(hist_data, bins=6, edgecolor='black')
            ax.set_title('Histogram')
            ax.set_xlabel('Wartość')
            ax.set_ylabel('Częstość')
            plt.show()
