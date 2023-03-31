from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlButton,
    ControlCombo,
    ControlDir,
    ControlList,
    )
import settings
from analisys import data
from views.FileChoose import FileChoose


class SimpleStats(BaseWidget):

   #Definition of the forms fields
    def __init__(self):
        super().__init__('Statystyka')

        settings.PYFORMS_STYLESHEET = './style.css'



