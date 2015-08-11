#
# Copyright (C) 2015 Tommy Alex. All Rights Reserved.
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
# intent constants for DroidUi

####################
# DroidFacede.Intent

# Standard Activity Actions
ACTION_MAIN = 'android.intent.action.MAIN'
ACTION_VIEW = 'android.intent.action.VIEW'
ACTION_ATTACH_DATA = 'android.intent.action.ATTACH_DATA'
ACTION_EDIT = 'android.intent.action.EDIT'
ACTION_PICK = 'android.intent.action.PICK'
ACTION_CHOOSER = 'android.intent.action.CHOOSER'
ACTION_GET_CONTENT = 'android.intent.action.GET_CONTENT'
ACTION_DIAL = 'android.intent.action.DIAL'
ACTION_CALL = 'android.intent.action.CALL'
ACTION_SEND = 'android.intent.action.SEND'
ACTION_SENDTO = 'android.intent.action.SENDTO'
ACTION_ANSWER = 'android.intent.action.ANSWER'
ACTION_INSERT = 'android.intent.action.INSERT'
ACTION_DELETE = 'android.intent.action.DELETE'
ACTION_RUN = 'android.intent.action.RUN'
ACTION_SYNC = 'android.intent.action.SYNC'
ACTION_PICK_ACTIVITY = 'android.intent.action.PICK_ACTIVITY'
ACTION_SEARCH = 'android.intent.action.SEARCH'
ACTION_WEB_SEARCH = 'android.intent.action.WEB_SEARCH'
ACTION_FACTORY_TEST = 'android.intent.action.FACTORY_TEST'

# Standard Broadcast Actions
ACTION_TIME_TICK = 'android.intent.action.TIME_TICK'
ACTION_TIME_CHANGED = 'android.intent.action.TIME_SET'
ACTION_TIMEZONE_CHANGED = 'android.intent.action.TIMEZONE_CHANGED'
ACTION_BOOT_COMPLETED = 'android.intent.action.BOOT_COMPLETED'
ACTION_PACKAGE_ADDED = 'android.intent.action.PACKAGE_ADDED'
ACTION_PACKAGE_CHANGED = 'android.intent.action.PACKAGE_CHANGED'
ACTION_PACKAGE_REMOVED = 'android.intent.action.PACKAGE_REMOVED'
ACTION_PACKAGE_RESTARTED = 'android.intent.action.PACKAGE_RESTARTED'
ACTION_PACKAGE_DATA_CLEARED = 'android.intent.action.PACKAGE_DATA_CLEARED'
ACTION_UID_REMOVED = 'android.intent.action.UID_REMOVED'
ACTION_BATTERY_CHANGED = 'android.intent.action.BATTERY_CHANGED'
ACTION_POWER_CONNECTED = 'android.intent.action.ACTION_POWER_CONNECTED'
ACTION_POWER_DISCONNECTED = 'android.intent.action.ACTION_POWER_DISCONNECTED'
ACTION_SHUTDOWN = 'android.intent.action.ACTION_SHUTDOWN'

# more action
ACTION_ADVANCED_SETTINGS_CHANGED = 'android.intent.action.ADVANCED_SETTINGS'
ACTION_AIRPLANE_MODE_CHANGED = 'android.intent.action.AIRPLANE_MODE'
ACTION_ALARM_CHANGED = 'android.intent.action.ALARM_CHANGED'
ACTION_ALL_APPS = 'android.intent.action.ALL_APPS'
ACTION_APPLICATION_RESTRICTIONS_CHANGED = 'android.intent.action.APPLICATION_RESTRICTIONS_CHANGED'
ACTION_APP_ERROR = 'android.intent.action.APP_ERROR'
ACTION_APP_FAILURE = 'com.tmobile.intent.action.APP_FAILURE'
ACTION_APP_FAILURE_RESET = 'com.tmobile.intent.action.APP_FAILURE_RESET'
ACTION_ASSIST = 'android.intent.action.ASSIST'
ACTION_BATTERY_LOW = 'android.intent.action.BATTERY_LOW'
ACTION_BATTERY_OKAY = 'android.intent.action.BATTERY_OKAY'
ACTION_BUG_REPORT = 'android.intent.action.BUG_REPORT'
ACTION_CALL_BUTTON = 'android.intent.action.CALL_BUTTON'
ACTION_CALL_EMERGENCY = 'android.intent.action.CALL_EMERGENCY'
ACTION_CALL_PRIVILEGED = 'android.intent.action.CALL_PRIVILEGED'
ACTION_CAMERA_BUTTON = 'android.intent.action.CAMERA_BUTTON'
ACTION_CLEAR_DNS_CACHE = 'android.intent.action.CLEAR_DNS_CACHE'
ACTION_CLOSE_SYSTEM_DIALOGS = 'android.intent.action.CLOSE_SYSTEM_DIALOGS'
ACTION_CONFIGURATION_CHANGED = 'android.intent.action.CONFIGURATION_CHANGED'
ACTION_CREATE_DOCUMENT = 'android.intent.action.CREATE_DOCUMENT'
ACTION_CREATE_SHORTCUT = 'android.intent.action.CREATE_SHORTCUT'
ACTION_DATE_CHANGED = 'android.intent.action.DATE_CHANGED'
ACTION_DEFAULT = 'android.intent.action.VIEW'
ACTION_DEVICE_STORAGE_FULL = 'android.intent.action.DEVICE_STORAGE_FULL'
ACTION_DEVICE_STORAGE_LOW = 'android.intent.action.DEVICE_STORAGE_LOW'
ACTION_DEVICE_STORAGE_NOT_FULL = 'android.intent.action.DEVICE_STORAGE_NOT_FULL'
ACTION_DEVICE_STORAGE_OK = 'android.intent.action.DEVICE_STORAGE_OK'
ACTION_DOCK_EVENT = 'android.intent.action.DOCK_EVENT'
ACTION_DOZE_PULSE_STARTING = 'android.intent.action.DOZE_PULSE_STARTING'
ACTION_DREAMING_STARTED = 'android.intent.action.DREAMING_STARTED'
ACTION_DREAMING_STOPPED = 'android.intent.action.DREAMING_STOPPED'
ACTION_EXTERNAL_APPLICATIONS_AVAILABLE = 'android.intent.action.EXTERNAL_APPLICATIONS_AVAILABLE'
ACTION_EXTERNAL_APPLICATIONS_UNAVAILABLE = 'android.intent.action.EXTERNAL_APPLICATIONS_UNAVAILABLE'
ACTION_GET_RESTRICTION_ENTRIES = 'android.intent.action.GET_RESTRICTION_ENTRIES'
ACTION_GLOBAL_BUTTON = 'android.intent.action.GLOBAL_BUTTON'
ACTION_GTALK_SERVICE_CONNECTED = 'android.intent.action.GTALK_CONNECTED'
ACTION_GTALK_SERVICE_DISCONNECTED = 'android.intent.action.GTALK_DISCONNECTED'
ACTION_HEADSET_PLUG = 'android.intent.action.HEADSET_PLUG'
ACTION_IDLE_MAINTENANCE_END = 'android.intent.action.ACTION_IDLE_MAINTENANCE_END'
ACTION_IDLE_MAINTENANCE_START = 'android.intent.action.ACTION_IDLE_MAINTENANCE_START'
ACTION_INPUT_METHOD_CHANGED = 'android.intent.action.INPUT_METHOD_CHANGED'
ACTION_INSERT_OR_EDIT = 'android.intent.action.INSERT_OR_EDIT'
ACTION_INSTALL_PACKAGE = 'android.intent.action.INSTALL_PACKAGE'
ACTION_KEYGUARD_WALLPAPER_CHANGED = 'android.intent.action.KEYGUARD_WALLPAPER_CHANGED'
ACTION_LOCALE_CHANGED = 'android.intent.action.LOCALE_CHANGED'
ACTION_MANAGED_PROFILE_ADDED = 'android.intent.action.MANAGED_PROFILE_ADDED'
ACTION_MANAGED_PROFILE_REMOVED = 'android.intent.action.MANAGED_PROFILE_REMOVED'
ACTION_MANAGE_NETWORK_USAGE = 'android.intent.action.MANAGE_NETWORK_USAGE'
ACTION_MANAGE_PACKAGE_STORAGE = 'android.intent.action.MANAGE_PACKAGE_STORAGE'
ACTION_MASTER_CLEAR = 'android.intent.action.MASTER_CLEAR'
ACTION_MEDIA_BAD_REMOVAL = 'android.intent.action.MEDIA_BAD_REMOVAL'
ACTION_MEDIA_BUTTON = 'android.intent.action.MEDIA_BUTTON'
ACTION_MEDIA_CHECKING = 'android.intent.action.MEDIA_CHECKING'
ACTION_MEDIA_EJECT = 'android.intent.action.MEDIA_EJECT'
ACTION_MEDIA_MOUNTED = 'android.intent.action.MEDIA_MOUNTED'
ACTION_MEDIA_NOFS = 'android.intent.action.MEDIA_NOFS'
ACTION_MEDIA_REMOVED = 'android.intent.action.MEDIA_REMOVED'
ACTION_MEDIA_SCANNER_FINISHED = 'android.intent.action.MEDIA_SCANNER_FINISHED'
ACTION_MEDIA_SCANNER_SCAN_FILE = 'android.intent.action.MEDIA_SCANNER_SCAN_FILE'
ACTION_MEDIA_SCANNER_STARTED = 'android.intent.action.MEDIA_SCANNER_STARTED'
ACTION_MEDIA_SHARED = 'android.intent.action.MEDIA_SHARED'
ACTION_MEDIA_UNMOUNTABLE = 'android.intent.action.MEDIA_UNMOUNTABLE'
ACTION_MEDIA_UNMOUNTED = 'android.intent.action.MEDIA_UNMOUNTED'
ACTION_MEDIA_UNSHARED = 'android.intent.action.MEDIA_UNSHARED'
ACTION_MY_PACKAGE_REPLACED = 'android.intent.action.MY_PACKAGE_REPLACED'
ACTION_NEW_OUTGOING_CALL = 'android.intent.action.NEW_OUTGOING_CALL'
ACTION_NEW_OUTGOING_SMS = 'android.intent.action.NEW_OUTGOING_SMS'
ACTION_OPEN_DOCUMENT = 'android.intent.action.OPEN_DOCUMENT'
ACTION_OPEN_DOCUMENT_TREE = 'android.intent.action.OPEN_DOCUMENT_TREE'
ACTION_PACKAGE_FIRST_LAUNCH = 'android.intent.action.PACKAGE_FIRST_LAUNCH'
ACTION_PACKAGE_FULLY_REMOVED = 'android.intent.action.PACKAGE_FULLY_REMOVED'
ACTION_PACKAGE_INSTALL = 'android.intent.action.PACKAGE_INSTALL'
ACTION_PACKAGE_NEEDS_VERIFICATION = 'android.intent.action.PACKAGE_NEEDS_VERIFICATION'
ACTION_PACKAGE_REPLACED = 'android.intent.action.PACKAGE_REPLACED'
ACTION_PACKAGE_VERIFIED = 'android.intent.action.PACKAGE_VERIFIED'
ACTION_PASTE = 'android.intent.action.PASTE'
ACTION_POWER_USAGE_SUMMARY = 'android.intent.action.POWER_USAGE_SUMMARY'
ACTION_PRE_BOOT_COMPLETED = 'android.intent.action.PRE_BOOT_COMPLETED'
ACTION_PROVIDER_CHANGED = 'android.intent.action.PROVIDER_CHANGED'
ACTION_QUERY_PACKAGE_RESTART = 'android.intent.action.QUERY_PACKAGE_RESTART'
ACTION_QUICK_CLOCK = 'android.intent.action.QUICK_CLOCK'
ACTION_REBOOT = 'android.intent.action.REBOOT'
ACTION_RECENTS_LONG_PRESS = 'android.intent.action.RECENTS_LONG_PRESS'
ACTION_REMOTE_INTENT = 'com.google.android.c2dm.intent.RECEIVE'
ACTION_REQUEST_SHUTDOWN = 'android.intent.action.ACTION_REQUEST_SHUTDOWN'
ACTION_RESTRICTIONS_CHALLENGE = 'android.intent.action.RESTRICTIONS_CHALLENGE'
ACTION_SCREEN_OFF = 'android.intent.action.SCREEN_OFF'
ACTION_SCREEN_ON = 'android.intent.action.SCREEN_ON'
ACTION_SEARCH_LONG_PRESS = 'android.intent.action.SEARCH_LONG_PRESS'
ACTION_SEND_MULTIPLE = 'android.intent.action.SEND_MULTIPLE'
ACTION_SET_WALLPAPER = 'android.intent.action.SET_WALLPAPER'
ACTION_SHOW_BRIGHTNESS_DIALOG = 'android.intent.action.SHOW_BRIGHTNESS_DIALOG'
ACTION_SYNC_STATE_CHANGED = 'android.intent.action.SYNC_STATE_CHANGED'
ACTION_SYSTEM_TUTORIAL = 'android.intent.action.SYSTEM_TUTORIAL'
ACTION_THEME_RESOURCES_CACHED = 'android.intent.action.THEME_RESOURCES_CACHED'
ACTION_UMS_CONNECTED = 'android.intent.action.UMS_CONNECTED'
ACTION_UMS_DISCONNECTED = 'android.intent.action.UMS_DISCONNECTED'
ACTION_UNINSTALL_PACKAGE = 'android.intent.action.UNINSTALL_PACKAGE'
ACTION_UPGRADE_SETUP = 'android.intent.action.UPGRADE_SETUP'
ACTION_USER_ADDED = 'android.intent.action.USER_ADDED'
ACTION_USER_BACKGROUND = 'android.intent.action.USER_BACKGROUND'
ACTION_USER_FOREGROUND = 'android.intent.action.USER_FOREGROUND'
ACTION_USER_INFO_CHANGED = 'android.intent.action.USER_INFO_CHANGED'
ACTION_USER_INITIALIZE = 'android.intent.action.USER_INITIALIZE'
ACTION_USER_PRESENT = 'android.intent.action.USER_PRESENT'
ACTION_USER_REMOVED = 'android.intent.action.USER_REMOVED'
ACTION_USER_STARTED = 'android.intent.action.USER_STARTED'
ACTION_USER_STARTING = 'android.intent.action.USER_STARTING'
ACTION_USER_STOPPED = 'android.intent.action.USER_STOPPED'
ACTION_USER_STOPPING = 'android.intent.action.USER_STOPPING'
ACTION_USER_SWITCHED = 'android.intent.action.USER_SWITCHED'
ACTION_VOICE_ASSIST = 'android.intent.action.VOICE_ASSIST'
ACTION_VOICE_COMMAND = 'android.intent.action.VOICE_COMMAND'
ACTION_WALLPAPER_CHANGED = 'android.intent.action.WALLPAPER_CHANGED'

# Standard Categories
CATEGORY_DEFAULT = 'android.intent.category.DEFAULT'
CATEGORY_BROWSABLE = 'android.intent.category.BROWSABLE'
CATEGORY_TAB = 'android.intent.category.TAB'
CATEGORY_ALTERNATIVE = 'android.intent.category.ALTERNATIVE'
CATEGORY_SELECTED_ALTERNATIVE = 'android.intent.category.SELECTED_ALTERNATIVE'
CATEGORY_LAUNCHER = 'android.intent.category.LAUNCHER'
CATEGORY_INFO = 'android.intent.category.INFO'
CATEGORY_HOME = 'android.intent.category.HOME'
CATEGORY_PREFERENCE = 'android.intent.category.PREFERENCE'
CATEGORY_TEST = 'android.intent.category.TEST'
CATEGORY_CAR_DOCK = 'android.intent.category.CAR_DOCK'
CATEGORY_DESK_DOCK = 'android.intent.category.DESK_DOCK'
CATEGORY_LE_DESK_DOCK = 'android.intent.category.LE_DESK_DOCK'
CATEGORY_HE_DESK_DOCK = 'android.intent.category.HE_DESK_DOCK'
CATEGORY_CAR_MODE = 'android.intent.category.CAR_MODE'
CATEGORY_APP_MARKET = 'android.intent.category.APP_MARKET'

# more category
CATEGORY_APP_BROWSER = 'android.intent.category.APP_BROWSER'
CATEGORY_APP_CALCULATOR = 'android.intent.category.APP_CALCULATOR'
CATEGORY_APP_CALENDAR = 'android.intent.category.APP_CALENDAR'
CATEGORY_APP_CONTACTS = 'android.intent.category.APP_CONTACTS'
CATEGORY_APP_EMAIL = 'android.intent.category.APP_EMAIL'
CATEGORY_APP_GALLERY = 'android.intent.category.APP_GALLERY'
CATEGORY_APP_MAPS = 'android.intent.category.APP_MAPS'
CATEGORY_APP_MESSAGING = 'android.intent.category.APP_MESSAGING'
CATEGORY_APP_MUSIC = 'android.intent.category.APP_MUSIC'
CATEGORY_DEVELOPMENT_PREFERENCE = 'android.intent.category.DEVELOPMENT_PREFERENCE'
CATEGORY_EMBED = 'android.intent.category.EMBED'
CATEGORY_FRAMEWORK_INSTRUMENTATION_TEST = 'android.intent.category.FRAMEWORK_INSTRUMENTATION_TEST'
CATEGORY_LEANBACK_LAUNCHER = 'android.intent.category.LEANBACK_LAUNCHER'
CATEGORY_LEANBACK_SETTINGS = 'android.intent.category.LEANBACK_SETTINGS'
CATEGORY_MONKEY = 'android.intent.category.MONKEY'
CATEGORY_OPENABLE = 'android.intent.category.OPENABLE'
CATEGORY_SAMPLE_CODE = 'android.intent.category.SAMPLE_CODE'
CATEGORY_THEME_PACKAGE_INSTALLED_STATE_CHANGE = 'com.tmobile.intent.category.THEME_PACKAGE_INSTALL_STATE_CHANGE'
CATEGORY_UNIT_TEST = 'android.intent.category.UNIT_TEST'
CATEGORY_VOICE = 'android.intent.category.VOICE'

# Standard Extra Data
EXTRA_ALARM_COUNT = 'android.intent.extra.ALARM_COUNT'
EXTRA_BCC = 'android.intent.extra.BCC'
EXTRA_CC = 'android.intent.extra.CC'
EXTRA_CHANGED_COMPONENT_NAME = 'android.intent.extra.changed_component_name'
EXTRA_DATA_REMOVED = 'android.intent.extra.DATA_REMOVED'
EXTRA_DOCK_STATE = 'android.intent.extra.DOCK_STATE'
EXTRA_DOCK_STATE_HE_DESK = 4
EXTRA_DOCK_STATE_LE_DESK = 3
EXTRA_DOCK_STATE_CAR = 2
EXTRA_DOCK_STATE_DESK = 1
EXTRA_DOCK_STATE_UNDOCKED = 0
EXTRA_DONT_KILL_APP = 'android.intent.extra.DONT_KILL_APP'
EXTRA_EMAIL = 'android.intent.extra.EMAIL'
EXTRA_INITIAL_INTENTS = 'android.intent.extra.INITIAL_INTENTS'
EXTRA_INTENT = 'android.intent.extra.INTENT'
EXTRA_KEY_EVENT = 'android.intent.extra.KEY_EVENT'
EXTRA_ORIGINATING_URI = 'android.intent.extra.ORIGINATING_URI'
EXTRA_PHONE_NUMBER = 'android.intent.extra.PHONE_NUMBER'
EXTRA_REFERRER = 'android.intent.extra.REFERRER'
EXTRA_REMOTE_INTENT_TOKEN = 'android.intent.extra.remote_intent_token'
EXTRA_REPLACING = 'android.intent.extra.REPLACING'
EXTRA_SHORTCUT_ICON = 'android.intent.extra.shortcut.ICON'
EXTRA_SHORTCUT_ICON_RESOURCE = 'android.intent.extra.shortcut.ICON_RESOURCE'
EXTRA_SHORTCUT_INTENT = 'android.intent.extra.shortcut.INTENT'
EXTRA_STREAM = 'android.intent.extra.STREAM'
EXTRA_SHORTCUT_NAME = 'android.intent.extra.shortcut.NAME'
EXTRA_SUBJECT = 'android.intent.extra.SUBJECT'
EXTRA_TEMPLATE = 'android.intent.extra.TEMPLATE'
EXTRA_TEXT = 'android.intent.extra.TEXT'
EXTRA_TITLE = 'android.intent.extra.TITLE'
EXTRA_UID = 'android.intent.extra.UID'

# more extra
EXTRA_ALLOW_MULTIPLE = 'android.intent.extra.ALLOW_MULTIPLE'
EXTRA_ALLOW_REPLACE = 'android.intent.extra.ALLOW_REPLACE'
EXTRA_ASSIST_CONTEXT = 'android.intent.extra.ASSIST_CONTEXT'
EXTRA_ASSIST_INPUT_HINT_KEYBOARD = 'android.intent.extra.ASSIST_INPUT_HINT_KEYBOARD'
EXTRA_ASSIST_PACKAGE = 'android.intent.extra.ASSIST_PACKAGE'
EXTRA_BUG_REPORT = 'android.intent.extra.BUG_REPORT'
EXTRA_CHANGED_COMPONENT_NAME_LIST = 'android.intent.extra.changed_component_name_list'
EXTRA_CHANGED_PACKAGE_LIST = 'android.intent.extra.changed_package_list'
EXTRA_CHANGED_UID_LIST = 'android.intent.extra.changed_uid_list'
EXTRA_CHOSEN_COMPONENT = 'android.intent.extra.CHOSEN_COMPONENT'
EXTRA_CHOSEN_COMPONENT_INTENT_SENDER = 'android.intent.extra.CHOSEN_COMPONENT_INTENT_SENDER'
EXTRA_CLIENT_INTENT = 'android.intent.extra.client_intent'
EXTRA_CLIENT_LABEL = 'android.intent.extra.client_label'
EXTRA_HTML_TEXT = 'android.intent.extra.HTML_TEXT'
EXTRA_INSTALLER_PACKAGE_NAME = 'android.intent.extra.INSTALLER_PACKAGE_NAME'
EXTRA_INSTALL_RESULT = 'android.intent.extra.INSTALL_RESULT'
EXTRA_KEY_CONFIRM = 'android.intent.extra.KEY_CONFIRM'
EXTRA_LOCAL_ONLY = 'android.intent.extra.LOCAL_ONLY'
EXTRA_MIME_TYPES = 'android.intent.extra.MIME_TYPES'
EXTRA_NOT_UNKNOWN_SOURCE = 'android.intent.extra.NOT_UNKNOWN_SOURCE'
EXTRA_ORIGINATING_UID = 'android.intent.extra.ORIGINATING_UID'
EXTRA_PACKAGES = 'android.intent.extra.PACKAGES'
EXTRA_REASON = 'android.intent.extra.REASON'
EXTRA_RECENTS_LONG_PRESS_RELEASE = 'android.intent.extra.RECENTS_LONG_PRESS_RELEASE'
EXTRA_REFERRER_NAME = 'android.intent.extra.REFERRER_NAME'
EXTRA_REMOVED_FOR_ALL_USERS = 'android.intent.extra.REMOVED_FOR_ALL_USERS'
EXTRA_REPLACEMENT_EXTRAS = 'android.intent.extra.REPLACEMENT_EXTRAS'
EXTRA_RESTRICTIONS_BUNDLE = 'android.intent.extra.restrictions_bundle'
EXTRA_RESTRICTIONS_INTENT = 'android.intent.extra.restrictions_intent'
EXTRA_RESTRICTIONS_LIST = 'android.intent.extra.restrictions_list'
EXTRA_RETURN_RESULT = 'android.intent.extra.RETURN_RESULT'
EXTRA_SHUTDOWN_USERSPACE_ONLY = 'android.intent.extra.SHUTDOWN_USERSPACE_ONLY'
EXTRA_THEME_PACKAGE_NAME = 'android.intent.extra.PACKAGE_NAME'
EXTRA_THEME_RESULT = 'android.intent.extra.RESULT'
EXTRA_TIME_PREF_24_HOUR_FORMAT = 'android.intent.extra.TIME_PREF_24_HOUR_FORMAT'
EXTRA_UNINSTALL_ALL_USERS = 'android.intent.extra.UNINSTALL_ALL_USERS'
EXTRA_USER = 'android.intent.extra.USER'
EXTRA_USER_HANDLE = 'android.intent.extra.user_handle'

# intent flags
FLAG_GRANT_READ_URI_PERMISSION = 1
FLAG_GRANT_WRITE_URI_PERMISSION = 2
FLAG_FROM_BACKGROUND = 4
FLAG_DEBUG_LOG_RESOLUTION = 8
FLAG_EXCLUDE_STOPPED_PACKAGES = 0x10
FLAG_INCLUDE_STOPPED_PACKAGES = 0x20
FLAG_GRANT_PERSISTABLE_URI_PERMISSION = 0x40
FLAG_GRANT_PREFIX_URI_PERMISSION = 0x80
FLAG_ACTIVITY_RETAIN_IN_RECENTS = 0x2000
FLAG_ACTIVITY_TASK_ON_HOME = 0x4000
FLAG_ACTIVITY_CLEAR_TASK = 0x8000
FLAG_ACTIVITY_NO_ANIMATION = 0x10000
FLAG_ACTIVITY_REORDER_TO_FRONT = 0x20000
FLAG_ACTIVITY_NO_USER_ACTION = 0x40000
FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET = 0x80000
FLAG_ACTIVITY_NEW_DOCUMENT = 0x80000
FLAG_ACTIVITY_LAUNCHED_FROM_HISTORY = 0x100000
FLAG_ACTIVITY_RESET_TASK_IF_NEEDED = 0x200000
FLAG_ACTIVITY_BROUGHT_TO_FRONT = 0x400000
FLAG_ACTIVITY_EXCLUDE_FROM_RECENTS = 0x800000
FLAG_ACTIVITY_PREVIOUS_IS_TOP = 0x1000000
FLAG_ACTIVITY_FORWARD_RESULT = 0x2000000
FLAG_ACTIVITY_CLEAR_TOP = 0x4000000
FLAG_RECEIVER_BOOT_UPGRADE = 0x4000000
FLAG_ACTIVITY_MULTIPLE_TASK = 0x8000000
FLAG_RECEIVER_REGISTERED_ONLY_BEFORE_BOOT = 0x8000000
FLAG_ACTIVITY_NEW_TASK = 0x10000000
FLAG_RECEIVER_FOREGROUND = 0x10000000
FLAG_ACTIVITY_SINGLE_TOP = 0x20000000
FLAG_RECEIVER_REPLACE_PENDING = 0x20000000
FLAG_ACTIVITY_NO_HISTORY = 0x40000000
FLAG_RECEIVER_REGISTERED_ONLY = 0x40000000

