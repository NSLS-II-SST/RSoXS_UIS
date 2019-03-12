from os import path
from pydm import Display

class I400Disp(Display):
	def __init__(self, parent=None, args=None, macros=None):
		super(I400Disp, self).__init__(parent=parent, args=args, macros=macros)
		self.ui.TimeSpan.valueChanged.connect(self.Time_changed)
		
	def Time_changed(self):
		self.tspan = self.ui.TimeSpan.value()
		self.ui.I400Plot.setTimeSpan(self.tspan)
		
	def ui_filename(self):
		# Point to our UI file
		return 'I400.ui'
		
	def ui_filepath(self):
		# Return the full path to the UI file
		return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())