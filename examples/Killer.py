#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Killer.py
# Manage running proc
#
# Author: Alex.wang
# Create: 2012-10-07 21:47


import sl4a
import DroidUi as Ui


def Killer():
	while True:
		all = Ui.Package.running()
		one = Ui.choose('Choose to kill', all)
		if one is None:
			break
		for name in one:
			print 'kill', name
			Ui.Package(name).stop()


if __name__ == '__main__':
	Killer()

