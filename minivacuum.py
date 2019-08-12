from os import path
from pydm import Display
from epics import caput

class minivacuum(Display):
    def __init__(self, parent=None, args=None, macros=None):
        super(minivacuum, self).__init__(parent=parent, args=args, macros=macros)
        self.ui.PyDMByteIndicator_8.clicked.connect(self.Psh7clicked)

    def Psh7clicked(self):
        if self.ui.PyDMByteIndicator_8.value() == 0:
            caput('XF:07IDA-PPS{PSh:7}Cmd:Opn-Cmd',1)
        else:
            caput('XF:07IDA-PPS{PSh:7}Cmd:Cls-Cmd', 1)


    def ui_filename(self):
        # Point to our UI file
        return 'RSoXSVacuumMINI.ui'

    def ui_filepath(self):
        # Return the full path to the UI file
        return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())