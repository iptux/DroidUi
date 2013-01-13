#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# DroidUiClass.py
# generate View classes in DroidUi.py
#
# Author: Alex.wang
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

