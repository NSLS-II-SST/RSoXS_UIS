from os import path
from pydm import Display

class MotorDisp(Display):
	def __init__(self, parent=None, args=None, macros=None):
		super(MotorDisp, self).__init__(parent=parent, args=args, macros=macros)
		self.ui.JogValue.valueChanged.connect(self.Jog_changed)
		
	def Jog_changed(self):
		self.jogvalue = self.ui.JogValue.value()
		self.ui.JogUp.updatePressValue(self.jogvalue)
		self.ui.JogDown.updatePressValue(-self.jogvalue)
		
	def ui_filename(self):
		# Point to our UI file
		return 'inline_motor.ui'
		
	def ui_filepath(self):
		# Return the full path to the UI file
		return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())