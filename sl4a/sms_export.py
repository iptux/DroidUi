# -*- coding: utf-8 -*-
#
# sms_export.py
# export all sms message
#
# Author: Alex.wang
# Create: 2012-07-27 20:55


import sl4a
import os, sys
from datetime import datetime


# number to contact map
contacts = {}

# name to fp map
sms_fp = {}

a = sl4a.sl4a()


def getContact(number, smsid = 0):
	global a, contacts
	if contacts.has_key(number):
		return contacts[number]
	try:
		r = a.queryContent('content://contacts/phones/filter/' + number)
		contacts[number] = r[0]
		return r[0]
	except:
		return {'name': 'sms_%d' % smsid, 'number': number}


def getSmsFp(contact):
	global sms_fp
	name = contact['name']
	try:
		return sms_fp[name]
	except:
		fname = contact['name'] + '.txt'
		# file name must be utf-8 encoded
		fp = open(fname.encode('utf-8'), 'w+')
		sms_fp[name] = fp
		# UnicodeDecodeError
		#print >>fp, 'name: %s\nnumber: %s\n' % (name.encode('gb18030'), contact['number'])
		print >>fp, 'name: %s' % name.encode('gb18030')
		print >>fp, 'number: %s\n' % contact['number']
		return fp


def sms(id):
	global a
	m = a.smsGetMessageById(id)
	fp = getSmsFp(getContact(m['address'], id))
	stamp = int(m['date'])
	print >>fp, 'stamp: %i' % stamp
	print >>fp, 'date: %s' % datetime.fromtimestamp(stamp/1000.0).strftime('%Y%m%d%H%M%S')
	print >>fp, 'body: %s\n' % m['body'].encode('gb18030')


def sms_all():
	global a
	l = a.smsGetMessageIds(0, '')
	l.sort()
	sum = len(l)
	for i in l:
		print '%i/%i' % (i, sum)
		sms(i)


def main():
	dir = 'sms_' + datetime.today().strftime('%Y%m%d')
	if not os.path.exists(dir):
		os.mkdir(dir)
	os.chdir(dir)
	sms_all()
	for f in sms_fp.itervalues():
		f.close()


if __name__ == '__main__':
	main()

