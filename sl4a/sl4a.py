# sl4a.py
# wrapper for android.Android()
#
# Author: Alex.Wang
# Create: 2012-02-05 23:36


from android import *


class sl4aError(Exception):
	pass


class sl4a(Android):
	def __getattr__(self, name):
		def rpc_call(*args):
			r = self._rpc(name, *args)
			if r.error:
				raise sl4aError, r.error
			return r.result
		return rpc_call
