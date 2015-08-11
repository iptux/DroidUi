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
# Symbolic constants for DroidUi


from ._intent import *
from ._keycode import *

#########
# DroidUi

try:
	type(basestring)
	XML_ENCODING = 'utf-8'
except NameError:	# basestring is removed in python 3
	basestring = str
	XML_ENCODING = 'unicode'

def isstring(obj):
	return isinstance(obj, basestring)

def stringlize(obj):
	'''stringlize an object'''
	return obj if isinstance(obj, basestring) else str(obj)

def joinattr(*attrs):
	'''join many attribute together'''
	return '|'.join(attrs)

def joinflags(*flags):
	'''join many flags together'''
	result = 0
	for flag in flags:
		result |= flag
	return result

# boolean
TRUE = 'true'
FALSE = 'false'

# layout_width and layout_height
WRAP_CONTENT = 'wrap_content'
MATCH_PARENT = 'match_parent'
FILL_PARENT = 'fill_parent'

# gravity and layout_gravity
TOP = 'top'
BOTTOM = 'bottom'
LEFT = 'left'
RIGHT = 'right'
CENTER = 'center'
FILL = 'fill'
CENTER_VERTICAL = 'center_vertical'
CENTER_HORIZONTAL = 'center_horizontal'
FILL_VERTICAL = 'fill_vertical'
FILL_HORIZONTAL = 'fill_horizontal'
CLIP_VERTICAL = 'clip_vertical'
CLIP_HORIZONTAL = 'clip_horizontal'

# misc
NONE = 'none'
HORIZONTAL = 'horizontal'
VERTICAL = 'vertical'

# visibility
VISIBLE = 'visible'
INVISIBLE = 'invisible'
GONE = 'gone'

# scrollbarStyle
INSIDE_OVERLAY = 'insideOverlay'
INSIDE_INSET = 'insideInset'
OUTSIDE_OVERLAY = 'outsideOverlay'
OUTSIDE_INSET = 'outsideInset'

# textStyle
NORMAL = 'normal'
BOLD = 'bold'
ITALIC = 'italic'

# typeface
SANS = 'sans'
SERIF = 'serif'
MONOSPACE = 'monospace'

# inputType
TEXT = 'text'
DATE = 'date'
TIME = 'time'
DATETIME = 'datetime'
PHONE = 'phone'
NUMBER = 'number'
NUMBER_SIGNED = 'numberSigned'
NUMBER_DECIMAL = 'numberDecimal'
TEXT_CAP_CHARACTERS = 'textCapCharacters'
TEXT_CAP_WORDS = 'textCapWords'
TEXT_CAP_SENTENCES = 'textCapSentences'
TEXT_AUTO_CORRECT = 'textAutoCorrect'
TEXT_AUTO_COMPLETE = 'textAutoComplete'
TEXT_MULTI_LINE = 'textMultiLine'
TEXT_IME_MULTI_LINE = 'textImeMultiLine'
TEXT_NO_SUGGESTIONS = 'textNoSuggestions'
TEXT_URI = 'textUri'
TEXT_EMAIL_ADDRESS = 'textEmailAddress'
TEXT_EMAIL_SUBJECT = 'textEmailSubject'
TEXT_SHORT_MESSAGE = 'textShortMessage'
TEXT_LONG_MESSAGE = 'textLongMessage'
TEXT_PERSON_NAME = 'textPersonName'
TEXT_POSTAL_ADDRESS = 'textPostalAddress'
TEXT_PASSWORD = 'textPassword'
TEXT_VISIBLE_PASSWORD = 'textVisiblePassword'
TEXT_WEB_EDIT_TEXT = 'textWebEditText'
TEXT_FILTER = 'textFilter'
TEXT_PHONETIC = 'textPhonetic'

#############
# DroidFacade

# SmsFacade
INBOX = 'inbox'

# Bluetooth
BLUETOOTH_UUID = '457807c0-4897-11df-9879-0800200c9a66'

# sensorNumber
SENSOR_ALL = 1
ORIENTATION = 1
ACCELEROMETER = 2
MAGNETOMETER = 3
LIGHT = 4

# axis parm
NO_AXIS = 0
X = 1
Y = 2
XY = 3
Z = 4
XZ = 5
YZ = 6
XYZ = 7

