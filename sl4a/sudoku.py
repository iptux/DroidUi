# -*- coding: utf-8 -*-
#
# sudoku.py
# sudoku game using DroidUi
#
# Author: Alex.Wang
# Create: 2012-09-17 21:27


import DroidUi as Ui
import DroidDialog as Dialog


class Game:
	back_color = '#ffffffff'
	puzzle_back = '#ffe6f0ff'
	hint_color = ['#64ff0000', '#6400ff80', '#2000ff80']
	def __init__(self, size = 9):
		self.value = [None] * (size * size)
		self.size = size
		self.haverun = False
		self.table = Ui.RelativeLayout(
			background = self.back_color,
			gravity = Ui.CENTER,
		)
		self.array = []
		row = [Ui.TextView(self.table,
					clickable = Ui.TRUE,
					command = lambda x = 0, y = 0: self.click(x, y),
					layout_width = '34dp',
					layout_height = '34dp',
					background = self.puzzle_back,
					layout_marginRight = '2dp',
					gravity = Ui.CENTER,
			)]
		for j in range(1, size):
			row.append(Ui.TextView(self.table,
				clickable = Ui.TRUE,
				command = lambda x = 0, y = j: self.click(x, y),
				layout_width = '34dp',
				layout_height = '34dp',
				background = self.puzzle_back,
				layout_toRightOf = '@id/' + row[j - 1].id,
				layout_marginRight = '2dp',
				gravity = Ui.CENTER,
			))
		self.array.append(row)
		for i in range(1, size):
			row = [Ui.TextView(self.table,
					clickable = Ui.TRUE,
					command = lambda x = i, y = 0: self.click(x, y),
					layout_width = '34dp',
					layout_height = '34dp',
					background = self.puzzle_back,
					layout_below = '@id/' + self.array[i - 1][0].id,
					layout_marginTop = '2dp',
					gravity = Ui.CENTER,
			)]
			for j in range(1, size):
				row.append(Ui.TextView(self.table,
					clickable = Ui.TRUE,
					command = lambda x = i, y = j: self.click(x, y),
					layout_width = '34dp',
					layout_height = '34dp',
					background = self.puzzle_back,
					layout_alignLeft = '@id/' + self.array[0][j].id,
					layout_alignTop = '@id/' + row[0].id,
					gravity = Ui.CENTER,
				))
			self.array.append(row)
	def _hint(self, x, y):
		l = len(self.tile(x, y))
		v = l < 3 and self.hint_color[l] or self.puzzle_back
		if v != self.array[x][y].get('background'):
			self.array[x][y].configure(background = v)
	def hint(self, x = None, y = None):
		if x and y:
			for i in range(self.size):
				self._hint(i, y)
			for j in range(self.size):
				self._hint(x, j)
			x1 = (x / 3) * 3
			y1 = (y / 3) * 3
			for i in range(x1, x1 + 3):
				for j in range(y1, y1 + 3):
					self._hint(i, j)
			return
		for i in range(self.size):
			for j in range(self.size):
				self._hint(i, j)
	def setvalue(self, value):
		if len(value) != self.size * self.size:
			print 'invalid puzzle:', value
			return
		for i in range(self.size):
			for j in range(self.size):
				v = int(value[i * self.size + j])
				self._set(i, j, v)
		self.hint()
	def tile(self, x, y):
		d = {}
		for i in range(1, self.size + 1):
			d[i] = True
		# vertical
		for i in range(self.size):
			if i == x: continue
			v = self.get(i, y)
			if v: d[v] = False
		# horizontal
		for j in range(self.size):
			if j == y: continue
			v = self.get(x, j)
			if v: d[v] = False
		# same cell block
		x1 = (x / 3) * 3
		y1 = (y / 3) * 3
		for i in range(x1, x1 + 3):
			for j in range(y1, y1 + 3):
				if i == x and j == y: continue
				v = self.get(i, j)
				if v: d[v] = False
		# 
		r = {}
		for v, b in d.iteritems():
			if b: r[v] = True
		return r
	def get(self, x, y):
		return self.value[ x * self.size + y ]
	def _set(self, x, y, value):
		if not value: value = ''
		self.value[ x * self.size + y ] = value
		self.array[x][y].configure(text = value)
	def set(self, x, y, value):
		self._set(x, y, value)
		self.hint(x, y)
	@staticmethod
	def getkey(valid):
		if 0 == len(valid):
			Dialog.info('no moves')
			return None
		return Dialog.pick('select', valid)
	def click(self, x, y):
		valid = self.tile(x, y).keys()
		valid.sort()
		ret = self.getkey(valid)
		if ret:
			self.set(x, y, ret)
	def main(self):
		self.haverun = True
		self.table.mainloop()


class Sudoku:
	about_text = '''Sudoku  is  a  logic-based  number  placement  puzzle.
Starting  with  a  partially  completed  9x9  grid,  the
objective  is  to  fill  the  grid  so  that  each
row,  each  column,  and  each  of  the  3x3  boxes
(also  called  blocks)  contains  the  digits
1  to  9  exactly  once.
'''
	Puzzle = {
	'easy': '360000000004230800000004200070460003820000014500013020001900000007048300000000045',
	'normal': '650000070000506000014000005007009000002314700000700800500000630000201000030000097',
	'hard': '009000000080605020501078000000000700706040102004000000000720903090301080000000600'}
	def __init__(self):
		self.about = Ui.TextView(
			Ui.ScrollView(
				padding = '20dp',
				background = '#ff000000'
			),
			text = self.about_text,
		)
		self.game = Game()
		self.outer = Ui.LinearLayout(
			Ui.LinearLayout(background = '#ff000000'),
			padding = '30dp',
			background = '#3500ffff',
			layout_height = Ui.FILL_PARENT,
		)
		self.inner = Ui.LinearLayout(self.outer, gravity = Ui.CENTER)
		Ui.TextView(self.inner,
			text = 'Android Sudoku',
			textSize = '24.5dip',
			layout_marginBottom = '25dip',
		)
		Ui.Button(self.inner, text = 'Continue', command = self.resume)
		Ui.Button(self.inner, text = 'New Game', command = self.play)
		Ui.Button(self.inner, text = 'About', command = self.about.mainloop)
		Ui.Button(self.inner, text = 'Exit', command = self.inner.quit)
	def resume(self):
		if self.game.haverun:
			self.game.main()
		else:
			self.play()
	def play(self):
		ret = Dialog.pick('New Game', ['easy', 'normal', 'hard'])
		if not ret:
			return
		self.game.setvalue(self.Puzzle[ret])
		self.game.main()
	def main(self):
		self.inner.mainloop('Sudoku')


if __name__ == '__main__':
	Sudoku().main()

