# DroidUi - a Python UI library for Android

Now Python is able to run on Android platform thanks to
[Scripting Layer for Android](https://code.google.com/p/android-scripting/)
and [python for android](https://code.google.com/p/python-for-android/)
project. But the [User Interface Facade](http://www.mithril.com.au/android/doc/UiFacade.html)
is hard to use. Most of the time, more than one call is needed to
achieve your simplest goal. And the 
[fullShow](https://code.google.com/p/android-scripting/wiki/ApiReference#fullShow)
call in [FullScreenUI](https://code.google.com/p/android-scripting/wiki/FullScreenUI)
need a XML style layout.

But what if you want to control the layout by programming,
or change the layout dynamically at run time?
I need a more elegant UI library, that is why [DroidUi](http://iptux.github.com/DroidUi/).


Quick Start
-----------

Let start with `Hello world` example,
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
* [Scripting Layer for Android](https://code.google.com/p/android-scripting/) [r6](https://code.google.com/p/android-scripting/downloads/detail?name=sl4a_r6.apk) and above installed.
* [python for android](https://code.google.com/p/python-for-android/) [r5](https://code.google.com/p/python-for-android/downloads/detail?name=PythonForAndroid_r5.apk) and above installed.


Install
-------

* make sure [adb](http://developer.android.com/tools/help/adb.html) is installed on your computer.
* connect your Android device to your computer.
* run _install.bat_(on Windows) or _install.sh_(on Linux).
* then DroidUi installed.


Links
-----

* [DroidUi](http://iptux.github.com/DroidUi/)
* [DroidUi Wiki](https://github.com/iptux/DroidUi/wiki)
* [python for android](https://code.google.com/p/python-for-android/)
* [Scripting Layer for Android](https://code.google.com/p/android-scripting/)

