# -*- coding: utf-8 -*-
#
# FlashLight.py
# a white screen that make the world brighter
#
# Author: Alex.wang
# Create: 2012-11-04 23:33


import DroidUi as Ui


def FlashLight():
	droid = Ui.DroidUi()

	try:
		# no screen dim
		droid.call('wakeLockAcquireBright')

		# set max screen brightness, but has no effect
		old_bright = droid.call('setScreenBrightness', 255)

		# show a white black screen
		gui = Ui.TextView(droid, background = '#ffffffff')
		gui.mainloop('FlashLight')

		# restore screen brightness
		droid.call('setScreenBrightness', old_bright)
	finally:
		droid.call('wakeLockRelease')


if __name__ == '__main__':
	FlashLight()


