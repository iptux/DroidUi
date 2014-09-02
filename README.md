# DroidUi - a Python UI library for Android

Now Python is able to run on Android platform thanks to
[Scripting Layer for Android][SL4A] and [Python for Android][Py4A]
project. But the [User Interface Facade][UiFacade]
is hard to use. Most of the time, more than one call is needed to
achieve your simplest goal. And the 
[fullShow][] call in [FullScreenUI][]
need a XML style layout.

But what if you want to control the layout by programming,
or change the layout dynamically at run time?
I need a more elegant UI library, that is why [DroidUi][].


Quick Start
-----------

Let's start with `Hello world` example,
```python
import DroidUi                                     # yes, you need it

layout = DroidUi.DroidUi()                         # layout object comes first
hello = DroidUi.Button(layout,                     # add this Button to the layout
                       text = 'Hello, DroidUi!',   # set the button text
                       command = layout.quit)      # quit the layout when button clicked
layout.mainloop()                                  # enter mainloop
```
Run this example will give you a big button full of your screen,
click button will quit this example.

There are mainly two kinds of object in `DroidUi`:
 * _layout_ objects: container of _View_, can be showed. (`DroidUi.DroidUi`)
 * _View_ objects: UI element, like View class in Android. (`DroidUi.View`)

DroidUi also support showing a layout from a existing XML layout,
use `DroidUi.DroidUi.fromxml()` and `DroidUi.DroidUi.fromfile()` to get the layout object


Requirement
-----------

* an Android device.
* [Scripting Layer for Android][SL4A] [r6][SL4A_r6] or above installed.
* [Python for Android][Py4A] [r5][Py4A_r5] or above installed.


Install
-------

* make sure [adb][] is installed on your computer.
* connect your Android device to your computer.
* run _install.bat_(on Windows) or _install.sh_(on Linux).
* then DroidUi installed.


License
-------

DroidUi is licensed under [GPLv3][] by Tommy Alex


Links
-----

* [DroidUi][]
* [DroidUi Wiki][Wiki]
* [Python for Android][Py4A]
* [Scripting Layer for Android][SL4A]



[SL4A]: https://code.google.com/p/android-scripting/
[Py4A]: https://code.google.com/p/python-for-android/
[UiFacade]: http://www.mithril.com.au/android/doc/UiFacade.html
[fullShow]: https://code.google.com/p/android-scripting/wiki/ApiReference#fullShow
[FullScreenUI]: https://code.google.com/p/android-scripting/wiki/FullScreenUI
[DroidUi]: http://iptux.github.com/DroidUi/
[SL4A_r6]: https://code.google.com/p/android-scripting/downloads/detail?name=sl4a_r6.apk
[Py4A_r5]: https://code.google.com/p/python-for-android/downloads/detail?name=PythonForAndroid_r5.apk
[adb]: http://developer.android.com/tools/help/adb.html
[Wiki]: https://github.com/iptux/DroidUi/wiki
[GPLv3]: http://www.gnu.org/copyleft/gpl.html

