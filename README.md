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

I need a more elegant UI library, that is why [DroidUi](http://iptux.github.com/DroidUi/).


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
