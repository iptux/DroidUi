# -*- coding: utf-8 -*-
#
# FlashLight.py
# a white screen that make the world brighter
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


def FlashLight():
	phone = Ui.Phone()
	lock = Ui.WakeLock()

	try:
		# no screen dim
		lock.bright()

		# set max screen brightness, but has no effect
		old_bright = phone.brightness(255)

		# show a white black screen
		gui = Ui.TextView(background = '#ffffffff')
		gui.mainloop('FlashLight')

		# restore screen brightness
		phone.brightness(old_bright)
	finally:
		lock.release()


if __name__ == '__main__':
	FlashLight()

