# -*- coding: utf-8 -*-
#
# another_fullscreenuiwrapper2demo.py
# reimpliment fullscreenuiwrapper2_demo.py using DroidUi
# original code: https://code.google.com/p/python-for-android/wiki/fullscreenwrapper2
#
# Author: Alex.wang
# Create: 2013-01-19 02:50


import random
import DroidUi as Ui


class DemoLayout:
	def __init__(self):
		self.layout = Ui.LinearLayout(
			background = "#ff314859",
			orientation = Ui.VERTICAL,
		)
		Ui.TextView(self.layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = "0px",
			textSize = "16dp",
			text = "FullScreenWrapper2 Demo",
			textColor = "#ffffffff",
			layout_weight = 20,
			gravity = Ui.CENTER,
		)
		self.txt_colorbox = Ui.TextView(self.layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = "0px",
			background = "#ff000000",
			layout_weight = "60",
			gravity = Ui.CENTER,
		)
		self.buttonBox = Ui.LinearLayout(self.layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = "0px",
			orientation = Ui.HORIZONTAL,
			layout_weight = "20",
		)
		Ui.Button(self.buttonBox,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			background = "#ff66a3d2",
			text = "Random Color",
			layout_weight = 1,
			textSize = "14dp",
			gravity = Ui.CENTER,
			# HERE: click callback, auto registered
			command = self.change_color,
		)
		Ui.Button(self.buttonBox,
			layout_width=Ui.FILL_PARENT,
			layout_height=Ui.FILL_PARENT,
			background = "#ff25567b",
			layout_weight = 1,
			text = "Exit",
			textSize = "14dp",
			gravity = Ui.CENTER,
			# HERE: call quit() on ui element will quit the current layout
			command = self.layout.quit,
		)

	def change_color(self):
		# 'Random Color' button click handler
		colorvalue = "#ff" + self.get_rand_hex_byte() + self.get_rand_hex_byte() + self.get_rand_hex_byte()
		self.txt_colorbox.configure(background = colorvalue)

	def get_rand_hex_byte(self):
		return '%02x' % random.randint(0,255)

	def mainloop(self):
		self.layout.mainloop()

if __name__ == '__main__':
	random.seed()
	DemoLayout().mainloop()

