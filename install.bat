@echo off

REM Copyright 2012-2013 by Tommy Alex. All Rights Reserved.
REM
REM Permission to use, copy, modify, and distribute this software and its
REM documentation for any purpose and without fee is hereby granted,
REM provided that the above copyright notice appear in all copies and that
REM both that copyright notice and this permission notice appear in
REM supporting documentation, and that the name of Vinay Sajip
REM not be used in advertising or publicity pertaining to distribution
REM of the software without specific, written prior permission.
REM VINAY SAJIP DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
REM ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
REM VINAY SAJIP BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
REM ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
REM IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
REM OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

REM install.bat
REM install DroidUi in your Android device

set sl4a=/sdcard/sl4a/scripts/

echo adb push DroidUi "%sl4a%DroidUi/"
echo adb push samples "%sl4a%"
