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

        self._button = ControlButton('Stwórz wykres')
        self._button.value = self.__runEvent

    def __runEvent(self):
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
            ax.set_title('My Graph')
            plt.show()

