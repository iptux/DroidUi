# -*- coding: utf-8 -*-
#
# txtReader.py
# try read txt file out
#
# Author: Alex.wang
# Create: 2012-09-06 22:31
#
# Update: 2012-09-07 21:01
#  1. 添加简单界面
#  2. 增加进度保存功能
#  3. 增加书架功能
# Update: 2012-09-08 11:54
#  1. 增加无声阅读模式


import os
import time
import ConfigParser
import sl4a


class txtReader:
	'''read txt file aloud'''
	TITLE = 'txtReader'
	CONFILE = 'txtReader.ini'
	SHELF = '/sdcard/book/'	# defalut book shelf directory
	def __init__(self):
		self.a = sl4a.sl4a()
		self.f = None
		self.conf = ConfigParser.ConfigParser()
		self.conf.read(self.CONFILE)
		self.stop = False
		self.sound = True
	def __del__(self):
		self.save()
		self.conf.write(open(self.CONFILE, 'wb+'))
		if self.f:
			self.f.close()
	def save(self):
		if not self.f:
			return
		n = self.f.name
		if not self.conf.has_section(n):
			self.conf.add_section(n)
		self.conf.set(n, 'offset', self.f.tell())
		self.conf.set(n, 'sound', self.sound)
	def progress(self, name):
		if self.conf.has_section(name):
			self.f.seek(self.conf.getint(name, 'offset'))
			self.sound = self.conf.getboolean(name, 'sound')
	def speak(self, what, block = False):
		'''speak message WHAT out, if BLOCK, return until speech end'''
		self.a.ttsSpeak(what)
		if block:
			# TODO: use a better way to block
			while self.a.ttsIsSpeaking():
				time.sleep(5)
	def display(self, msg):
		'''display book content'''
		self.a.dialogCreateAlert(os.path.basename(self.f.name), msg)
		self.a.dialogSetPositiveButtonText('有声')
		self.a.dialogSetNeutralButtonText('无声')
		self.a.dialogSetNegativeButtonText('停止')
		self.a.dialogShow()
	def handle(self):
		'''decide continue or not'''
		if not self.sound:
			r = self.a.dialogGetResponse()
		else:
			e = self.a.eventPoll()
			if len(e) == 0:
				return
			r = e[0]['data']
		if r.has_key('which'):
			result = r['which']
			if result == 'positive':
				self.sound = True
			elif result == 'neutral':
				self.sound = False
			elif result == 'negative':
				self.stop = True
		elif r.has_key('canceled'):
			self.stop = True
		else:
			print 'Unknown response=', r
	def read(self, what):
		'''"read" one line'''
		print what
		self.display(what)
		if self.sound:
			self.speak(what, True)
		self.handle()
	def loop(self):
		'''loop over a file'''
		self.a.wakeLockAcquirePartial()
		self.a.eventClearBuffer()
		try:
			while not self.stop:
				line = self.f.readline()
				if not line:	# end of file
					self.f.seek(0)
					return
				line = line.strip()
				if not line:	# empty line
					continue
				self.read(line)
		finally:
			self.save()
			self.f.close()
			self.f = None
			self.a.wakeLockRelease()
	def book(self, fname):
		self.f = open(fname, 'rb')
		self.progress(fname)
		self.loop()
	def choose(self, title, items):
		'''choose from items'''
		self.a.dialogCreateAlert(title)
		self.a.dialogSetItems(items)
		self.a.dialogShow()
		r = self.a.dialogGetResponse()
		return r.has_key('item') and items[r['item']] or None
	def bookshelf(self):
		'''get a book from bookshelf'''
		txt = []
		for i in os.listdir(self.SHELF):
			path = os.path.join(self.SHELF, i)
			if os.path.isfile(path) and path.endswith('.txt'):
				txt.append(i)
		r = self.choose('选择书籍', txt)
		return r and os.path.join(self.SHELF, r) or None
	def history(self):
		'''get a book from history'''
		return self.choose('继续阅读', self.conf.sections())
	def about(self):
		'''show about dialog'''
		self.a.dialogCreateAlert(self.TITLE, 'txtReader 0.1\nAlex.wang\niptux7@gmail.com')
		self.a.dialogSetNegativeButtonText('关闭')
		self.a.dialogShow()
		self.a.dialogGetResponse()
	def welcome(self):
		'''show welcome dialog'''
		self.a.dialogCreateAlert(self.TITLE, '欢迎使用 txtReader')
		self.a.dialogSetPositiveButtonText('书架')
		self.a.dialogSetNeutralButtonText('历史')
		self.a.dialogSetNegativeButtonText('关于')
		self.a.dialogShow()
		r = self.a.dialogGetResponse()
		if not r.has_key('which'):	# 返回键，退出
			quit()
		return {'positive': self.bookshelf,
		'neutral': self.history,
		'negative': self.about}[r['which']]()
	def main(self):
		while True:
			b = self.welcome()
			if b is None:
				continue
			self.book(b)


if __name__ == '__main__':
	txtReader().main()

