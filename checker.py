#!/usr/bin/env python3

"""checker.py: Checking the environment readiness."""

__author__       = "Daniel Baktiar"
__copyright__    = "Copyright 2021, Daniel Baktiar"
__credits__      = ["Daniel Baktiar"]
__license__      = "Apache"
__version__      = "1.0.1"
__maintainer__   = "Daniel Baktiar"
__email__        = "dbaktiar@gmail.com"
__status__       = "Development"


class Checker(object):
	"""
	Checker class.
	"""

	def __init__(self):
		"""
		Initialize the class Checker.
		"""
		pass

	def check(self):
		"""
		perform the check
		"""
		print('checking...')


if __name__ == '__main__':
	"""
	the main invocation point.
	"""
	checker = Checker()
	checker.check()

