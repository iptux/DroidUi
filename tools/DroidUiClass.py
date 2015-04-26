#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# DroidUiClass.py
# generate View classes in DroidUi.py
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
# Create: 2012-09-16 14:18


def DroidUiClass():
	out = open('DroidUiClass.out', 'wb+')
	parent = [None] * 10
	parent[-1] = '_View'
	for line in open('DroidUiClass.txt'):
		line = line.rstrip()
		info = line.lstrip()
		diff = len(line) - len(info)
		l = info.split(' ')
		name = l[0]
		parent[diff] = name
		print >>out, "class %s(%s):" % ( name, parent[diff - 1] )
		print >>out, "\twidgetName = '%s'" % ( name[0] == '_' and name[1:] or name )
		if len(l) > 1:
			print >>out, "\tdefaultConfig = {"
			for i in range(1, len(l), 2):
				print >>out, "\t\t'%s': %s," % (l[i], l[i + 1])
			print >>out, "\t}"
		print >>out


if __name__ == '__main__':
	DroidUiClass()

