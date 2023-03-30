from pyforms.basewidget import BaseWidget
from pyforms.controls   import (
    ControlButton,
    ControlCombo,
    ControlDir,
    ControlList,
    )

from pyforms            import settings

class FileChoose(BaseWidget):
   #Definition of the forms fields
    def __init__(self):
        super().__init__('Analiza danych dot. chorób serca 2')

if __name__ == "__main__":

    from pyforms import start_app
    start_app(FileChoose, geometry=(660,300,660,200))