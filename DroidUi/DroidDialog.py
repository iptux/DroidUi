# Copyright 2012-2013 by Tommy Alex. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Vinay Sajip
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# VINAY SAJIP DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# VINAY SAJIP BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

'''dialog wrapper function for UiFacade
'''

import datetime
from sl4a import sl4a
from DroidConstants import TEXT, TEXT_PASSWORD, NUMBER_SIGNED, NUMBER_DECIMAL
from DroidConstants import stringlize


# you can change them for custom Button text
YES = 'Yes'
NO = 'No'
OK = 'OK'
CANCEL = 'Cancel'


class _Dialog(object):
	'''basic dialog for android'''
	DialogType = {
		'alert': 'dialogCreateAlert',
		'date': 'dialogCreateDatePicker',
		'progress': 'dialogCreateHorizontalProgress',
		'input': 'dialogCreateInput',
		'password': 'dialogCreatePassword',
		'seekbar': 'dialogCreateSeekBar',
		'spinner': 'dialogCreateSpinnerProgress',
		'time': 'dialogCreateTimePicker',
	}

	def __init__(self):
		if not hasattr(_Dialog, '_a'):
			setattr(_Dialog, '_a', sl4a())
		self.result = None

	def call(self, func, *args):
		'''wrapper for sl4a.sl4a'''
		return getattr(self._a, func)(*args)

	def create(self, type, *args):
		'''create dialog, for TYPE, see DialogType'''
		self.call(self.DialogType[type], *args)

	def buttons(self, yes = YES, no = NO, cancel = None):
		'''set button text'''
		if yes: self.call('dialogSetPositiveButtonText', stringlize(yes))
		if no: self.call('dialogSetNegativeButtonText', stringlize(no))
		if cancel: self.call('dialogSetNeutralButtonText', stringlize(cancel))

	def list(self, items, multi = False):
		'''set list items for dialog'''
		if multi: self.call('dialogSetMultiChoiceItems', items)
		else: self.call('dialogSetSingleChoiceItems', items)

	def update(self, value):
		'''update progress'''
		self.call('dialogSetCurrentProgress', value)

	def show(self):
		'''show dialog'''
		self.call('dialogShow')

	def response(self):
		'''get dialog response'''
		return self.call('dialogGetResponse')

	def selected(self):
		'''get select items'''
		return self.call('dialogGetSelectedItems')

	def dismiss(self):
		'''dismiss dialog'''
		self.call('dialogDismiss')

	def yes(self, data):
		'''Positive button click callback function'''
		self.result = data

	def no(self, data):
		'''Negative button click callback function'''
		pass

	def cancel(self, data):
		'''Neutral button click callback function'''
		pass

	def back(self, data):
		'''BACK key click callback function'''
		self.cancel(data)

	def handle(self):
		'''handle dialog event'''
		_Handler = {
			'positive': self.yes,
			'neutral': self.cancel,
			'negative': self.no,
		}
		data = self.response()
		if data.has_key('which'):
			_Handler[data['which']](data)
		elif data.has_key('canceled'):
			self.back(data)
		else:
			print 'Unknown response = ', data

	def main(self):
		self.handle()
		self.dismiss()

def _merge(d, **kw):
	# set default value for dict
	for k, v in kw.iteritems():
		d.setdefault(k, v)

###############################################################
# input dialog

def _askstring(title, message, default, type, **kw):
	d = _Dialog()
	d.create('input', title, message, stringlize(default), type)
	_merge(kw, yes = OK, no = CANCEL)
	d.buttons(**kw)
	d.show()
	d.main()
	r = None
	if d.result: r = d.result['value']
	return r

def askstring(title, message, default = '', **kw):
	return _askstring(title, message, default, TEXT, **kw)

def askpassword(title, message, default = '', **kw):
	return _askstring(title, message, default, TEXT_PASSWORD, **kw)

def askint(title, message, default = 0, **kw):
	return int(_askstring(title, message, default, NUMBER_SIGNED, **kw))

def askfloat(title, message, default = 0.0, **kw):
	return float(_askstring(title, message, default, NUMBER_DECIMAL, **kw))

###############################################################
# seekbar

def askvalue(title, message, value = 50, max = 100, **kw):
	'''get a value using seekbar'''
	d = _Dialog()
	d.create('seekbar', value, max, title, message)
	_merge(kw, yes = OK, no = CANCEL)
	d.buttons(**kw)
	d.show()
	d.main()
	r = None
	if d.result: r = d.result['progress']
	return r

###############################################################
# date dialog

def askdate(date = None):
	'''get a date, if DATE is None, using today as default'''
	if date is None: date = datetime.date.today()
	d = _Dialog()
	d.create('date', date.year, date.month, date.day)
	d.show()
	d.main()
	r = d.result
	if r: r = datetime.date(r['year'], r['month'], r['day'])
	return r

###############################################################
# time dialog

def asktime(time = None):
	'''get a time, if TIME is None, using now as default
	NOTE: only hour and minute is supported'''
	if time is None: time = datetime.datetime.now().time()
	d = _Dialog()
	d.create('time', time.hour, time.minute, True)
	d.show()
	d.main()
	r = d.result
	if r: r = datetime.time(r['hour'], r['minute'])
	return r

###############################################################
# list items

def _choose(title, items, multi, **kw):
	d = _Dialog()
	d.create('alert', title)
	d.list(items, multi)
	_merge(kw, yes = OK, no = CANCEL)
	d.buttons(**kw)
	d.show()
	d.handle()
	if d.result is None: return None
	r = d.selected()
	if multi: return tuple([ items[i] for i in r ])
	else: return items[r[0]]

def select(title, items, **kw):
	'''select one item from ITEMS
	RETURN: the selected item, or None if cancelled'''
	return _choose(title, items, False, **kw)

def choose(title, items, **kw):
	'''choose one or more items from ITEMS
	RETURN: a tuple of chosen items, or None if cancelled'''
	return _choose(title, items, True, **kw)

def pick(title, items):
	'''choose one items from ITEMS
	RETURN:  the selected item, or None if cancelled'''
	d = _Dialog()
	d.create('alert', title)
	d.call('dialogSetItems', items)
	d.show()
	r = d.response()
	return r.has_key('item') and items[r['item']] or None

###############################################################
# alert dialog

class _Alert(_Dialog):

	def __init__(self, title, message, yes, no, cancel = None):
		_Dialog.__init__(self)
		self.create('alert', title, message)
		self.buttons(yes, no, cancel)
		self.show()

	def yes(self, data):
		self.result = True

	def no(self, data):
		self.result = False

def message(title, message, text = OK):
	'''show a message'''
	_Alert(title, message, text, None).main()

def askyesno(title, message, **kw):
	'''ask yes or no
	RETURN: True on Yes, False on No, or None if cancelled'''
	_merge(kw, yes = YES, no = NO)
	d = _Alert(title, message, kw['yes'], kw['no'])
	d.main()
	return d.result

def askyesnocancel(title, message, **kw):
	'''ask yes or no or cancel
	RETURN: True on Yes, False on No, or None if cancelled'''
	_merge(kw, yes = YES, no = NO, cancel = CANCEL)
	d = _Alert(title, message, kw['yes'], kw['no'], kw['cancel'])
	d.main()
	return d.result

def info(what):
	'''show information INFO to user'''
	_Dialog().call('makeToast', what)

def notify(title, message):
	'''Displays a notification'''
	_Dialog().call('notify', title, message)

###############################################################
# progress dialog

class _Progress(object):
	def __init__(self, title, message, max, type):
		self.d = _Dialog()
		self.d.create(type, title, message, max)
	def show(self):
		self.d.show()
	def update(self, value):
		self.d.update(value)
	def dismiss(self):
		self.d.dismiss()

def Progress(title, message, max = 100):
	'''get a Horizontal Progress dialog'''
	return _Progress(title, message, max, 'progress')

def Loading(title, message, max = 100):
	'''get a Spinner Progress dialog'''
	return _Progress(title, message, max, 'spinner')

###############################################################
# test

if __name__ == '__main__':
	# a sample use of Progress dialog
	import time
	p = Progress('DroidDialog', 'Sample usage of Progress Bar', 300)
	p.show()
	for i in range(30):
		time.sleep(0.1)
		p.update(i * 10)
	p.dismiss()
	print 'done'

