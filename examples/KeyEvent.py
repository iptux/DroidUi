# -*- coding: utf-8 -*-
#
# KeyEvent.py
# show Key Event
#
# Author: Alex.wang
# Create: 2012-11-04 23:33


import DroidUi as Ui


def display_event(data):
	text = 'Key %s is pressed' % data['key']
	view.config(text = text)
	return True


def main():
	global view
	gui = Ui.DroidUi()
	view = Ui.TextView(gui,
		text = 'Press any key',
		textSize = '40sp',
		layout_width = Ui.FILL_PARENT,
		gravity = Ui.CENTER,
	)
	Ui.Button(gui, text = 'Quit', command = gui.quit)
	gui.reg_event('key', display_event)
	gui.mainloop()


if __name__ == '__main__':
	main()

