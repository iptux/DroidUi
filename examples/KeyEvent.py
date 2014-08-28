# -*- coding: utf-8 -*-
#
# KeyEvent.py
# show Key Event
#
# Copyright (C) 2012-2014 Tommy Alex. All Rights Reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
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

