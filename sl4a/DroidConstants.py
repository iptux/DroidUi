# Symbolic constants for DroidUi

# boolean
TRUE = 'true'
FALSE = 'false'

# key
BACK = 4
UP = 19
LEFT = 20
RIGHT = 21
DOWN = 22
VOLUME_UP = 24
VOLUME_DOWN = 25
MENU = 82
SEARCH = 84

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
