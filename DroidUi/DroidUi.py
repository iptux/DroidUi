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

'''Wrapper functions for FullScreenUi
(http://code.google.com/p/android-scripting/wiki/FullScreenUI)

DroidUi provides classes which alow the display, positioning and
control of widgets.

Properties of the widgets are specified with keyword arguments.
Keyword arguments have the same name as the corresponding resource
under android.

'''


import warnings
import xml.etree.ElementTree as ET
import sl4a
from DroidConstants import *


class _writableString:
	'''writable string'''
	def __init__(self, str = ''):
		self.set(str)
	def set(self, str):
		self.buffer = str
	def write(self, what):
		self.buffer += what
	def __str__(self):
		return self.buffer


def noneHandler(data = None):
	'''none handler, do nothing'''
	return True


class DroidUi:
	'''layout object, like layout resource in android project'''
	namespace = 'http://schemas.android.com/apk/res/android'
	def __init__(self):
		self._root = None
		self._oldroot = None
		self._loop = True
		self.showed = False
		self.objmap = {}
		self._isLayoutDirty = True
		self._xmlLayout = ''
		self.title = None
		self._click_cb = {}
		self._key_cb = {BACK: self.quit, MENU: noneHandler}
		self._optionMenu = []
		self._handler = {
			'click': self._click,
			'key': self._key,
			'screen': self._screen,
		}
		if not hasattr(DroidUi, '_a'):
			setattr(DroidUi, '_a', sl4a.sl4a())
	@staticmethod
	def _parse(element, master):
		'''build view object from xml Elememt'''
		for elem in element.getchildren():
			attrib = {}
			id = None
			for k, v in elem.items():
				# remove namespace mark
				if k.find(DroidUi.namespace) != -1:
					k = k[len(DroidUi.namespace) + 2:]
				# id
				if k == 'id':
					id = v = v[v.find('/') + 1:]
				# set attrib
				attrib[k] = v
			exec 'view = %s(master, attrib)' % elem.tag
			if id:
				setattr(view.droid, id, view)
			# iter children
			DroidUi._parse(elem, view)
		return master
	@staticmethod
	def fromxml(xml):
		'''build layout object from a string contains xml data'''
		return DroidUi._parse(ET.fromstring(xml), DroidUi())
	@staticmethod
	def fromfile(source):
		'''build layout object from a xml file
		SOURCE may be a filename or file object'''
		return DroidUi._parse(ET.parse(source).getroot(), DroidUi())
	def _screen(self, data):
		'''screen event handler'''
		if data == 'destroy':
			# ignore it first
			#self.quit()
			return True
	def _click(self, data):
		'''click event handler'''
		_id = data['id']
		if self._click_cb.has_key(_id):
			self._click_cb[_id]()
			return True
	def _key(self, data):
		'''key event handler'''
		key = int(data['key'])
		if self._key_cb.has_key(key):
			self._key_cb[key]()
			return True
	def call(self, fun, *arg):
		'''sl4a call wrapper'''
		return getattr(self._a, fun)(*arg)
	def reg_obj(self, id, obj):
		'''register widget objects'''
		if self.objmap.has_key(id): warnings.warn('two widget has same id(%s): %s, %s', id, str(obj), str(self.objmap[id]))
		self.objmap[id] = obj
	def unreg_obj(self, id):
		'''unregister widget objects'''
		if not self.objmap.has_key(id): warnings.warn('no widget has this id: %s', id)
		else: del self.objmap[id]
	def _setroot(self, root):
		'''set root element of the layout'''
		# the first root element
		if self._root is None:
			self._root = root
		# second element, wrap them in a LinearLayout
		elif self._oldroot is None:
			self._oldroot = self._root
			self._root = LinearLayout(self, background = '#ff000000')
			self._oldroot._setroot(self._root)
			root._setroot(self._root)
			self._root.append(self._oldroot)
			self._root.append(root)
		# the third and more, add them to LinearLayout like the first two
		elif self._root is not self._oldroot:
			root._setroot(self._root)
			self._root.append(root)
	def reg_click_cb(self, id, callback):
		'''register click event handler
		if widget with id ID is clicked, then CALLBACK will be called'''
		assert callable(callback)
		if self._click_cb.has_key(id): warnings.warn('click callback is override: id = %s' % id)
		self._click_cb[id] = callback
	def reg_key_cb(self, key, callback, override = False):
		'''register key event handler
		if key KEY is pressed, then CALLBACK will be called

		if OVERRRIDE is True, the key's default behaviour will be overrided
		by default, BACK key quit current layout, MENU key shows menu if there's one'''
		assert callable(callback)
		if self._key_cb.has_key(key): warnings.warn('key callback is override: key = %d' % key)
		self._key_cb[key] = callback
		if override: self._a.fullKeyOverride([key])
	def reg_event(self, name, handler):
		'''register event handler
		HANDLER should accept 1 param which contains event data
		HANDLER should return True if the event is handled properly'''
		assert callable(handler)
		if self._handler.has_key(name): warnings.warn('event handler is override: ev = %s' % name)
		self._handler[name] = handler
	def quit(self, data = None):
		'''quit event loop
		there is a DATA parameter, so quit can be used as a event handler as well as a click handler or key handler'''
		self._loop = False
		return True
	def addOptionMenu(self, text, command, event = None, data = None, icon = None):
		'''add an option menu item, after MENU key pressed
		TEXT    - text of the menu
		COMMAND - callback function if menu item clicked
		EVENT   - event generated if menu item clicked
		DATA    - parameter passed to COMMAND on called
		ICON    - Android system menu icon.
		for icon, see http://developer.android.com/reference/android/R.drawable.html'''
		if not event: event = text
		if not data: data = event
		self.reg_event(event, command)
		self._optionMenu.append((text, event, data, icon))
	def _eventLoop(self, n):
		'''event handling loop'''
		if n == 0: self._a.eventClearBuffer()
		while self._loop:
			event = self._a.eventWait()
			name = event["name"]
			if self._handler.has_key(name):
				if not self._handler[name](event['data']):
					warnings.warn('unhandled event: %s' % str(event))
			else:
				warnings.warn('unknown event: %s' % str(event))
		# allow reentry
		self._loop = True
	def _setdirty(self):
		'''set the layout is dirty, so when show(), layout needs to be regenerated'''
		self._isLayoutDirty = True
	def updateLayout(self):
		'''update the xml content stands for this layout'''
		# no need to update layout
		if not self._isLayoutDirty: return

		if self._root is None: self._root = TextView(self, text = "You havn't set any View for this layout :(", padding = '30dp')
		self._root.set('xmlns:android', DroidUi.namespace)
		tree = ET.ElementTree(self._root)
		layout = _writableString()
		tree.write(layout)
		self._xmlLayout = str(layout)
		self._isLayoutDirty = False
	def showHook(self):
		'''called right after layout showed'''
		pass
	def _show(self):
		'''show the layout on screen'''
		self.updateLayout()

		if self.title is not None:
			self._a.fullShow(self._xmlLayout, self.title)
		else:
			self._a.fullShow(self._xmlLayout)
		self.showed = True
		self.showHook()

		self._a.clearOptionsMenu()
		for m in self._optionMenu:
			self._a.addOptionsMenuItem(*m)
	def mainloop(self, title = None):
		'''main loop'''
		# support serial call to mainloop
		if not hasattr(DroidUi, 'n'):
			setattr(DroidUi, 'n', 0)
			setattr(DroidUi, 'queue', [self])
		else:
			DroidUi.n += 1
			DroidUi.queue.append(self)

		if title is not None: self.title = title
		self._show()

		try: self._eventLoop(DroidUi.n)
		finally:
			self.showed = False
			# if this is the last screen, just quit
			if 0 == DroidUi.n:
				self._a.fullDismiss()
			# or, show previous screen
			else:
				DroidUi.queue[DroidUi.n - 1]._show()
			DroidUi.n -= 1


class _View(ET._Element):
	'''View element'''
	widgetName = ''
	defaultConfig = {}
	def __init__(self, master = None, cnf = {}, **kw):
		ET._Element.__init__(self, self.widgetName, {})

		# combine all configure together
		cnf = cnf.copy()
		for k, v in self.defaultConfig.iteritems():
			cnf.setdefault(k, v)
		if len(kw): cnf.update(kw)

		if master is None: master = DroidUi()
		if isinstance(master, DroidUi):
			master._setroot(self)
			self.root = self
			self.droid = master
		else:
			master.append(self)
			self.root = master.root
			self.droid = master.droid
		self.master = master

		if cnf.has_key('id'):
			self.setid(cnf['id'])
			del cnf['id']
		else: self.setid('%s#%x' % (self.widgetName, id(self)) )

		self.config(**cnf)
	def set(self, key, value):
		if key.find(':') == -1: key = "android:%s" % key
		if not isinstance(value, unicode):
			value = str(value)
		ET._Element.set(self, key, value)
	def get(self, key, default = None):
		return ET._Element.get(self, "android:%s" % key, default)
	def setid(self, id):
		'''set widget id'''
		if hasattr(self, 'id') and self.id:
			self.droid.unreg_obj(self.id)
		self.id = id
		self.set('id', '@+id/' + id)
		self.droid.reg_obj(id, self)
	def _setroot(self, root):
		self.root = root
		for child in self:
			child._setroot(root)
	def key(self, key, handler):
		'''set key handler'''
		self.droid.reg_key_cb(key, handler)
	def focus(self):
		'''require focus on this view'''
		if self.droid.showed: warnings.warn('focus required after showed: %s', str(self))
		else: self.append(ET.Element('requestFocus', {}))
	def _property(self, key, value):
		if not self.droid.showed: return
		if not isinstance(value, unicode): value = str(value)
		self.droid.call('fullSetProperty', self.id, key, value)
	def configure(self, **kw):
		'''configure view properties'''
		# command is used as click handler
		if kw.has_key('command'):
			self.droid.reg_click_cb(self.id, kw['command'])
			del kw['command']
		showed = self.droid.showed
		for k, v in kw.items():
			self.set(k, v)
			self.droid._setdirty()
			if showed:
				self._property(k, v)
	config = configure
	def cget(self, key, default = None):
		'''get property value'''
		value = None
		if self.droid.showed:
			try: value = self.droid.call('fullQueryDetail', self.id)[key]
			except KeyError: pass
		if value is None:
			value = self.get(key, default)
		return value
	def mainloop(self, title = None):
		self.droid.mainloop(title)
	def quit(self, data = None):
		return self.droid.quit(data)


#####################################################################
# View classes, the inherit tree is same as android

class View(_View):
	widgetName = 'View'
	defaultConfig = {
		'layout_width': WRAP_CONTENT,
		'layout_height': WRAP_CONTENT,
	}

class AnalogClock(View):
	widgetName = 'AnalogClock'

class CalendarView(View):
	widgetName = 'CalendarView'

class DayView(CalendarView):
	widgetName = 'DayView'

class WeekView(CalendarView):
	widgetName = 'WeekView'

class ComposingView(View):
	widgetName = 'ComposingView'

class DragView(View):
	widgetName = 'DragView'

class ImageView(View):
	widgetName = 'ImageView'

class AnimatedImageView(ImageView):
	widgetName = 'AnimatedImageView'

class CheckableImageView(ImageView):
	widgetName = 'CheckableImageView'

class ImageButton(ImageView):
	widgetName = 'ImageButton'

class ZoomButton(ImageButton):
	widgetName = 'ZoomButton'

class ProgressBar(View):
	widgetName = 'ProgressBar'

class _AbsSeekBar(ProgressBar):
	widgetName = 'AbsSeekBar'

class RatingBar(_AbsSeekBar):
	widgetName = 'RatingBar'

class SeekBar(_AbsSeekBar):
	widgetName = 'SeekBar'

class TextView(View):
	widgetName = 'TextView'

class ActionMenuButton(TextView):
	widgetName = 'ActionMenuButton'

class Button(TextView):
	widgetName = 'Button'
	defaultConfig = {
		'layout_width': FILL_PARENT,
		'layout_height': WRAP_CONTENT,
	}

class CompoundButton(Button):
	widgetName = 'CompoundButton'

class CheckBox(CompoundButton):
	widgetName = 'CheckBox'

class RadioButton(CompoundButton):
	widgetName = 'RadioButton'

class ToggleButton(CompoundButton):
	widgetName = 'ToggleButton'

class ExtractButton(Button):
	widgetName = 'ExtractButton'

class CheckedTextView(TextView):
	widgetName = 'CheckedTextView'

class Chronometer(TextView):
	widgetName = 'Chronometer'

class DateView(TextView):
	widgetName = 'DateView'

class DigitalClock(TextView):
	widgetName = 'DigitalClock'

class EditText(TextView):
	widgetName = 'EditText'
	defaultConfig = {
		'layout_width': MATCH_PARENT,
		'layout_height': WRAP_CONTENT,
	}

class AutoCompleteTextView(EditText):
	widgetName = 'AutoCompleteTextView'

class MultiAutoCompleteTextView(AutoCompleteTextView):
	widgetName = 'MultiAutoCompleteTextView'

class MockView(TextView):
	widgetName = 'MockView'

class MapView(MockView):
	widgetName = 'MapView'

class SurfaceView(MockView):
	widgetName = 'SurfaceView'

class VideoView(SurfaceView):
	widgetName = 'VideoView'

class WebView(MockView):
	widgetName = 'WebView'

class ViewGroup(View):
	widgetName = 'ViewGroup'
	defaultConfig = {
		'layout_width': MATCH_PARENT,
		'layout_height': MATCH_PARENT,
	}

class AbsoluteLayout(ViewGroup):
	widgetName = 'AbsoluteLayout'

class SlideView(AbsoluteLayout):
	widgetName = 'SlideView'

class _AdapterView(ViewGroup):
	widgetName = 'AdapterView'

class _AbsListView(_AdapterView):
	widgetName = 'AbsListView'

class GridView(_AbsListView):
	widgetName = 'GridView'

class ListView(_AbsListView):
	widgetName = 'ListView'

class ExpandableListView(ListView):
	widgetName = 'ExpandableListView'

class _AbsSpinner(_AdapterView):
	widgetName = 'AbsSpinner'

class Gallery(_AbsSpinner):
	widgetName = 'Gallery'

class Spinner(_AbsSpinner):
	widgetName = 'Spinner'

class FrameLayout(ViewGroup):
	widgetName = 'FrameLayout'

class DatePicker(FrameLayout):
	widgetName = 'DatePicker'

class GestureOverlayView(FrameLayout):
	widgetName = 'GestureOverlayView'

class HorizontalScrollView(FrameLayout):
	widgetName = 'HorizontalScrollView'

class MediaController(FrameLayout):
	widgetName = 'MediaController'

class ScrollView(FrameLayout):
	widgetName = 'ScrollView'

class TabHost(FrameLayout):
	widgetName = 'TabHost'

class TimePicker(FrameLayout):
	widgetName = 'TimePicker'

class ViewAnimator(FrameLayout):
	widgetName = 'ViewAnimator'

class ViewFlipper(ViewAnimator):
	widgetName = 'ViewFlipper'

class ViewSwitcher(ViewAnimator):
	widgetName = 'ViewSwitcher'

class ImageSwitcher(ViewSwitcher):
	widgetName = 'ImageSwitcher'

class TextSwitcher(ViewSwitcher):
	widgetName = 'TextSwitcher'

class LinearLayout(ViewGroup):
	widgetName = 'LinearLayout'
	defaultConfig = {
		'orientation': 'vertical',
		'layout_width': MATCH_PARENT,
		'layout_height': WRAP_CONTENT,
	}

class RadioGroup(LinearLayout):
	widgetName = 'RadioGroup'

class TableLayout(LinearLayout):
	widgetName = 'TableLayout'

class TableRow(LinearLayout):
	widgetName = 'TableRow'

class TabWidget(LinearLayout):
	widgetName = 'TabWidget'

class ZoomControls(LinearLayout):
	widgetName = 'ZoomControls'

class RelativeLayout(ViewGroup):
	widgetName = 'RelativeLayout'

class DialerFilter(RelativeLayout):
	widgetName = 'DialerFilter'

class TwoLineListItem(RelativeLayout):
	widgetName = 'TwoLineListItem'

class SlidingDrawer(ViewGroup):
	widgetName = 'SlidingDrawer'

class ViewStub(View):
	widgetName = 'ViewStub'


#####################################################################
# test code

if __name__ == '__main__':
	def callback(data = 'hello'):
		print data
		return True
	droid = DroidUi()
	layout = TextView(droid, text = 'Hello')
	EditText(droid, text = 'hello', command = callback)
	Button(droid, text = 'Quit', command = droid.quit)
	droid.addOptionMenu('Menu', callback)
	droid.addOptionMenu('Exit', droid.quit)
	droid.mainloop()

