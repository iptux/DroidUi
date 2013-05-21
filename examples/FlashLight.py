# -*- coding: utf-8 -*-
#
# FlashLight.py
# a white screen that make the world brighter
#
# Author: Alex.wang
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
		gui = Ui.TextView(droid, background = '#ffffffff')
		gui.mainloop('FlashLight')

		# restore screen brightness
		phone.brightness(old_bright)
	finally:
		lock.release()


if __name__ == '__main__':
	FlashLight()

