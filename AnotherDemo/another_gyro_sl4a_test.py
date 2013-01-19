# -*- coding: utf-8 -*-
#
# another_gyro_sl4a_test.py
# reimpliment gyro_sl4a_test.py using DroidUi
# original code: https://code.google.com/p/python-for-android/wiki/fullscreenwrapper2
#
# Author: Alex.wang
# Create: 2013-01-19 23:33


import math
import DroidUi as Ui


color_bg = "#ff314859"
color_default = "#ff66a3d2"
color_white = '#ffffffff'


class GyroTestLayout(Ui.DroidUi):
	def __init__(self):
		Ui.DroidUi.__init__(self)
		self.layout = Ui.LinearLayout(self,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			background = color_bg,
			orientation = Ui.VERTICAL,
		)
	
		Ui.TextView(self.layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = "0px",
			textSize = "20dp",
			text = "Gyro Test",
			textColor = color_white,
			layout_weight = 19,
			gravity = Ui.CENTER,
		)

		box1 = self._boxLayout(self.layout)
		self._block(box1, color_bg)
		self.txt_top = self._block(box1, color_default)
		self._block(box1, color_bg)

		box2 = self._boxLayout(self.layout)
		self.txt_left = self._block(box2, color_default)
		self._block(box2, color_bg)
		self.txt_right = self._block(box2, color_default)

		box3 = self._boxLayout(self.layout)
		self._block(box3, color_bg)
		self.txt_bottom = self._block(box3, color_default)
		self._block(box3, color_bg)

		self.reg_event('sensors', self.gyro)

	def _boxLayout(self, master):
		return Ui.LinearLayout(master,
			layout_width = Ui.FILL_PARENT,
			layout_height = "0px",
			orientation = Ui.HORIZONTAL,
			layout_weight = 27,
		)

	def _block(self, master, color):
		return Ui.TextView(master,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			layout_weight = 1,
			gravity = Ui.CENTER,
			background = color,
		)

	def gyro(self, data):
		value = int(data["pitch"] * 60.0 / math.pi * 2)
		color, basecolor = self.get_color(value)
		if value > 0:
			self.txt_top.configure(background = color)
			self.txt_bottom.configure(background = basecolor)
		else:
			self.txt_top.configure(background = basecolor)
			self.txt_bottom.configure(background = color)

		value = int(data["roll"] * 60.0 / math.pi * 4)
		color, basecolor = self.get_color(value)
		if value > 0:
			self.txt_right.configure(background = color)
			self.txt_left.configure(background = basecolor)
		else:
			self.txt_right.configure(background = basecolor)
			self.txt_left.configure(background = color)

		# mark event as handled
		return True

	colorvals = ["#ff66a3d2","#FF63BE7B", "#FF83C77D","#FFA2D07F", "#FFC1DA81", "#FFE0E383", "#FFFFEB84", "#FFFDD17F", "#FFFCB77A", "#FFFA9D75", "#FFF98370", "#FFF8696B"]

	def get_color(self, value):
		value = abs(value)
		if value > 59:
			value = 59
		return self.colorvals[int(value/5)], self.colorvals[0]


if __name__ == '__main__':
	gui = GyroTestLayout()
	gui.call('startSensingTimed', 1, 200)
	gui.mainloop()
	gui.call('stopSensing')

