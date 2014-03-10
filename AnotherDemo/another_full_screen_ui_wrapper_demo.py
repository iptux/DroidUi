# -*- coding: utf-8 -*-
#
# another_full_screen_ui_wrapper_demo.py
# reimpliment full_screen_ui_wrapper_demo.py using DroidUi
# original code: https://code.google.com/p/python-for-android/wiki/FullScreenWrapper
#
# Author: Alex.wang
# Create: 2013-01-19 02:50


from datetime import datetime
import DroidUi as Ui


color_light = "#ff66a3d2"
color_deep = "#ff25567b"
color_white = "#ffffffff"
color_yellow = "#ffffff00"


class add_screen(Ui.DroidUi):
	# add_screen layout
	def __init__(self):
		Ui.DroidUi.__init__(self)
		self.result = None
		self.curdatetime = datetime.today()

		self.layout = Ui.LinearLayout(self,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			background = "#ff314859",
			orientation = Ui.VERTICAL,
		)

		Ui.TextView(self.layout,
			layout_width = Ui.FILL_PARENT,
			textSize = "20dp",
			text = "Add Screen",
			textColor = color_white,
			gravity = Ui.CENTER,
			layout_weight = 15,
		)

		self._datetimeLayout(self.layout, 'add_txt_date', 'Date', self.on_but_datechange_click)
		self._datetimeLayout(self.layout, 'add_txt_time', 'Time', self.on_but_timechange_click)

		valueLayout = Ui.LinearLayout(self.layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.WRAP_CONTENT,
			orientation = Ui.HORIZONTAL,
			layout_weight = 11,
		)
		Ui.TextView(valueLayout,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			text = 'Value',
			textColor = color_yellow,
			textSize = "14dp",
			layout_weight = 1,
			gravity = Ui.CENTER,
			textStyle = 1,
		)
		self.add_txt_value = Ui.EditText(valueLayout,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			digits = "0123456789",
			textSize = "12dp",
			layout_weight = 1,
			background = color_white,
			gravity = Ui.joinattr(Ui.LEFT, Ui.CENTER_VERTICAL),
		)
		Ui.Button(valueLayout,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			textColor = color_yellow,
			textSize = "14dp",
			layout_weight = 1,
			background = color_light,
			text = "Save",
			gravity = Ui.CENTER,
			command = self.on_but_save_click,
		)

		Ui.TextView(self.layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.WRAP_CONTENT,
			textSize = "10dp",
			text = "Type value or choose below",
			textColor = color_white,
			gravity = Ui.CENTER,
			layout_weight = 5,
		)

		buttonBox1 = self._buttonLayout(self.layout)
		self._valueButton(buttonBox1, 40, color_light)
		self._valueButton(buttonBox1, 70, color_deep)
		self._valueButton(buttonBox1, 100, color_light)
		self._valueButton(buttonBox1, 120, color_deep)

		buttonBox2 = self._buttonLayout(self.layout)
		self._valueButton(buttonBox2, 150, color_deep)
		self._valueButton(buttonBox2, 180, color_light)
		self._valueButton(buttonBox2, 200, color_deep)
		self._valueButton(buttonBox2, 250, color_light)

		buttonBox3 = self._buttonLayout(self.layout)
		self._valueButton(buttonBox3, 300, color_light)
		self._valueButton(buttonBox3, 350, color_deep)
		self._valueButton(buttonBox3, 400, color_light)
		self._valueButton(buttonBox3, 450, color_deep)

	def _datetimeLayout(self, master, name, text, command):
		layout = Ui.LinearLayout(master,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.WRAP_CONTENT,
			orientation = Ui.HORIZONTAL,
			layout_weight = 11,
		)
		Ui.TextView(layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			text = text,
			textColor = color_yellow,
			textSize = "14dp",
			layout_weight = 1,
			gravity = Ui.CENTER,
			textStyle = 1,
		)
		setattr(self, name, Ui.TextView(layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			textColor = color_white,
			textSize = "14dp",
			layout_weight = 1,
			gravity = Ui.joinattr(Ui.LEFT, Ui.CENTER_VERTICAL),
		))
		Ui.Button(layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			textColor = color_white,
			textSize = "14dp",
			layout_weight = 1,
			background = color_light,
			text = "Change",
			gravity = Ui.CENTER,
			command = command,
		)
		Ui.LinearLayout(master,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.WRAP_CONTENT,
			layout_weight = 1,
		)

	def _buttonLayout(self, master):
		return Ui.LinearLayout(master,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.WRAP_CONTENT,
			orientation = Ui.HORIZONTAL,
			layout_weight = 15,
		)

	def _valueButton(self, master, value, background):
		return Ui.Button(master,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			text = value,
			textSize = "14dp",
			background = background,
			textColor = color_white,
			layout_weight = 1,
			gravity = Ui.CENTER,
			command = lambda value = value: self.on_but_value_handler(value),
		)

	def on_but_save_click(self):
		valuetext = self.add_txt_value.cget('text', '')

		if valuetext and valuetext.isdigit():
			self.result = '%s:00 - %s' % (self.curdatetime.isoformat(' ')[:16], valuetext)
			self.layout.quit()
		else:
			Ui.info("You must enter a valid number for calories")

	def on_but_datechange_click(self):
		newdate = Ui.askdate(self.curdatetime.date())
		if newdate:
			self.curdatetime = datetime.combine(newdate, self.curdatetime.timetz())
			self.add_txt_date.configure(text = self.curdatetime.date().isoformat())

	def on_but_timechange_click(self):
		newtime = Ui.asktime(self.curdatetime.time())
		if newtime:
			self.curdatetime = datetime.combine(self.curdatetime.date(), newtime)
			self.add_txt_time.configure(text = self.curdatetime.time().isoformat()[:5])

	def on_but_value_handler(self, value):
		self.add_txt_value.configure(text = value)

	def showHook(self):
		self.add_txt_date.configure(text = self.curdatetime.date().isoformat())
		self.add_txt_time.configure(text = self.curdatetime.time().isoformat()[:5])


class main_screen(Ui.DroidUi):
	show_list = ["2012-05-02 21:30:00 - 500","2012-05-02 20:00:00 - 100","2012-05-02 19:30:00 - 200"]

	def __init__(self):
		Ui.DroidUi.__init__(self)

		self.layout = Ui.LinearLayout(self,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.FILL_PARENT,
			background = "#ff314859",
			orientation = Ui.VERTICAL,
		)
		Ui.TextView(self.layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.WRAP_CONTENT,
			text = "Wrapper Demo",
			textSize = "20dp",
			gravity = Ui.CENTER,
			textColor = color_yellow,
		)
		self.lst_list = Ui.ListView(self.layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = "300dp",
		)
		self.buttonBox = Ui.LinearLayout(self.layout,
			layout_width = Ui.FILL_PARENT,
			layout_height = Ui.WRAP_CONTENT,
			orientation = Ui.HORIZONTAL,
		)
		self._button(self.buttonBox,
			text = "Add",
			background = color_light,
			command = self.on_but_add_click,
		)
		self._button(self.buttonBox,
			text = "Lookup",
			background = color_deep,
			command = self.on_but_lookup,
		)
		self._button(self.buttonBox,
			text = "Exit",
			background = color_light,
			command = self.layout.quit,
		)

	def showHook(self):
		self.lst_list.setlist(self.show_list)

	def _button(self, master, **kw):
		Ui.Button(master,
			layout_width = Ui.FILL_PARENT,
			layout_height = "80dp",
			textSize = "14dp",
			textColor = color_white,
			layout_weight = 1,
			gravity = Ui.CENTER,
			**kw
		)

	def on_but_add_click(self):
		add_screen_inst = add_screen()
		add_screen_inst.mainloop()
		item = add_screen_inst.result
		if item:
			self.show_list.insert(0, item)
			self.showHook()

	def on_but_lookup(self):
		Ui.info("no functionality built yet :-)")


if __name__ == '__main__':
	main_screen().mainloop()


