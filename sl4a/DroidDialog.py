'''dialog wrapper function for UiFacade
'''

import datetime
import sl4a
from DroidConstants import *


class _Dialog:
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
			setattr(_Dialog, '_a', sl4a.sl4a())
		self.result = None
	def call(self, func, *args):
		'''wrapper for sl4a.sl4a'''
		return getattr(self._a, func)(*args)
	def create(self, type, *args):
		'''create dialog, for TYPE, see DialogType'''
		self.call(self.DialogType[type], *args)
	def buttons(self, yes = 'Yes', no = 'No', cancel = None):
		'''set button text'''
		if yes: self.call('dialogSetPositiveButtonText', str(yes))
		if no: self.call('dialogSetNegativeButtonText', str(no))
		if cancel: self.call('dialogSetNeutralButtonText', str(cancel))
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

###############################################################
# input dialog

def _askstring(title, message, default, type):
	d = _Dialog()
	d.create('input', title, message, str(default), type)
	d.buttons('OK', 'Cancel')
	d.show()
	d.main()
	return d.result['value']

def askstring(title, message, default = ''):
	return _askstring(title, message, default, TEXT)

def askpassword(title, message, default = ''):
	return _askstring(title, message, default, TEXT_PASSWORD)

def askint(title, message, default = 0):
	return int(_askstring(title, message, default, NUMBER_SIGNED))

def askfloat(title, message, default = 0.0):
	return float(_askstring(title, message, default, NUMBER_DECIMAL))

###############################################################
# seekbar

def askvalue(title, message, value = 50, max = 100):
	'''get a value using seekbar'''
	d = _Dialog()
	d.create('seekbar', value, max, title, message)
	d.buttons('OK', 'Cancel')
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

def _choose(title, items, multi):
	d = _Dialog()
	d.create('alert', title)
	d.list(items, multi)
	d.buttons('OK', 'Cancel')
	d.show()
	d.handle()
	if d.result is None: return None
	r = d.selected()
	if multi: return tuple([ items[i] for i in r ])
	else: return items[r[0]]

def select(title, items):
	'''select one item from ITEMS
	RETURN: the selected item, or None if cancelled'''
	return _choose(title, items, False)

def choose(title, items):
	'''choose one or more items from ITEMS
	RETURN: a tuple of chosen items, or None if cancelled'''
	return _choose(title, items, True)

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

def message(title, message, text = 'OK'):
	'''show a message'''
	_Alert(title, message, text, None).main()

def askyesno(title, message):
	'''ask yes or no
	RETURN: True on Yes, False on No, or None if cancelled'''
	d = _Alert(title, message, 'Yes', 'No')
	d.main()
	return d.result

def askyesnocancel(title, message):
	'''ask yes or no or cancel
	RETURN: True on Yes, False on No, or None if cancelled'''
	d = _Alert(title, message, 'Yes', 'No', 'Cancel')
	d.main()
	return d.result

###############################################################
# progress dialog

class _Progress:
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

def Spinner(title, message, max = 100):
	'''get a Spinner Progress dialog'''
	return _Progress(title, message, max, 'spinner')

###############################################################
# test

if __name__ == '__main__':
	# a sample use of Progress dialog
	import time
	p = Progress('title', 'Progress Bar', 300)
	p.show()
	for i in range(30):
		time.sleep(0.1)
		p.update(i * 10)
	print 'done'
	p.dismiss()

