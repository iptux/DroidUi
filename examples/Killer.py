#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Killer.py
# Manage running proc
#
# Copyright (C) 2012-2015 Tommy Alex. All Rights Reserved.
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
# Create: 2012-10-07 21:47


import DroidUi as Ui


def Killer():
	while True:
		all = Ui.Package.running()
		one = Ui.choose('Choose to kill', all)
		if one is None:
			break
		for name in one:
			print('kill', name)
			Ui.Package(name).stop()


if __name__ == '__main__':
	Killer()

