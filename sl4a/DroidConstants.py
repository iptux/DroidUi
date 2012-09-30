# Symbolic constants for DroidUi

# boolean
TRUE = 'true'
FALSE = 'false'

# key
KEY_UNKNOWN = 0
KEY_SOFT_LEFT = 1
KEY_SOFT_RIGHT = 2
HOME = KEY_HOME = 3
BACK = KEY_BACK = 4
KEY_CALL = 5
KEY_ENDCALL = 6
KEY_0 = 7
KEY_1 = 8
KEY_2 = 9
KEY_3 = 10
KEY_4 = 11
KEY_5 = 12
KEY_6 = 13
KEY_7 = 14
KEY_8 = 15
KEY_9 = 16
KEY_STAR = 17
KEY_POUND = 18
KEY_DPAD_UP = 19
KEY_DPAD_DOWN = 20
KEY_DPAD_LEFT = 21
KEY_DPAD_RIGHT = 22
KEY_DPAD_CENTER = 23
VOLUME_UP = KEY_VOLUME_UP = 24
VOLUME_DOWN = KEY_VOLUME_DOWN = 25
KEY_POWER = 26
KEY_CAMERA = 27
KEY_CLEAR = 28
KEY_A = 29
KEY_B = 30
KEY_C = 31
KEY_D = 32
KEY_E = 33
KEY_F = 34
KEY_G = 35
KEY_H = 36
KEY_I = 37
KEY_J = 38
KEY_K = 39
KEY_L = 40
KEY_M = 41
KEY_N = 42
KEY_O = 43
KEY_P = 44
KEY_Q = 45
KEY_R = 46
KEY_S = 47
KEY_T = 48
KEY_U = 49
KEY_V = 50
KEY_W = 51
KEY_X = 52
KEY_Y = 53
KEY_Z = 54
KEY_COMMA = 55
KEY_PERIOD = 56
KEY_ALT_LEFT = 57
KEY_ALT_RIGHT = 58
KEY_SHIFT_LEFT = 59
KEY_SHIFT_RIGHT = 60
KEY_TAB = 61
KEY_SPACE = 62
KEY_SYM = 63
KEY_EXPLORER = 64
KEY_ENVELOPE = 65
KEY_ENTER = 66
KEY_DEL = 67
KEY_GRAVE = 68
KEY_MINUS = 69
KEY_EQUALS = 70
KEY_LEFT_BRACKET = 71
KEY_RIGHT_BRACKET = 72
KEY_BACKSLASH = 73
KEY_SEMICOLON = 74
KEY_APOSTROPHE = 75
KEY_SLASH = 76
KEY_AT = 77
KEY_NUM = 78
KEY_HEADSETHOOK = 79
KEY_FOCUS = 80
KEY_PLUS = 81
MENU = KEY_MENU = 82
KEY_NOTIFICATION = 83
SEARCH = KEY_SEARCH = 84
KEY_MEDIA_PLAY_PAUSE = 85
KEY_MEDIA_STOP = 86
KEY_MEDIA_NEXT = 87
KEY_MEDIA_PREVIOUS = 88
KEY_MEDIA_REWIND = 89
KEY_MEDIA_FAST_FORWARD = 90
KEY_MUTE = 91

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
FILL = 'FILL'
CENTER_VERTICAL = 'center_vertical'
CENTER_HORIZONTAL = 'center_horizontal'
FILL_VERTICAL = 'fill_vertical'
FILL_HORIZONTAL = 'fill_horizontal'
CLIP_VERTICAL = 'clip_vertical'
CLIP_HORIZONTAL = 'clip_horizontal'

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

# visibility
VISIBLE = 'visible'
INVISIBLE = 'invisible'
GONE = 'gone'

# misc
NONE = 'none'
HORIZONTAL = 'horizontal'
VERTICAL = 'vertical'


def joinattr(*attrs):
	'''join many attribute together'''
	return '|'.join(attrs)
