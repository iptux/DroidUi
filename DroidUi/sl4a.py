#
# Copyright (C) 2012-2014 Tommy Alex. All Rights Reserved.
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
# sl4a.py
# wrapper for android.Android()
#
# Create: 2012-02-05 23:36


from android import *


class sl4aError(Exception):
	pass


class sl4a(Android):
	'''make the android.Android class more pythonic'''
	def __getattr__(self, name):
		def rpc_call(*args):
			r = self._rpc(name, *args)
			if r.error:
				raise sl4aError(r.error)
			return r.result
		return rpc_call

# used internally by DroidUi
_a = sl4a()

