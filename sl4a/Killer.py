#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Killer.py
# Manage running proc
#
# Author: Alex.wang
# Create: 2012-10-07 21:47


import sl4a
import DroidDialog as Dialog


class Killer:
	def __init__(self):
		self.a = sl4a.sl4a()
	def kill(self, name):
		print 'kill', name
		self.a.forceStopPackage(name)
	def get(self):
		return self.a.getRunningPackages()
	def main(self):
		while True:
			all = self.get()
			one = Dialog.choose('Choose to kill', all)
			if one is None:
				break
			for i in one:
				self.kill(i)


if __name__ == '__main__':
	Killer().main()

