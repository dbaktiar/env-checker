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


import socket
import yaml


class Checker(object):
	"""
	Checker class.
	"""

	def __init__(self):
		"""
		Initialize the class Checker.
		"""
		pass

	def open_socket(self, host, port):
		"""
		Open and check if there is a listening socket in the (host, port)
		"""
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print('connecting to %s:%d...' % (host, port,))
		s.connect((host, port,))
		s.close()
		print('done.')


	def check_with_config_yaml(self, config_yaml='default.yaml'):
		"""
		perform the check
		"""
		print('reading yaml config file [%s]...' % (config_yaml,))
		with open(r'default.yaml') as yaml_file:
			check_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)
			print(check_yaml)
		for service in check_yaml['check-services']:
			print('checking services [%s]...' % (service['name']))
			error_happened = False
			host = service['host']
			port = int(service['port'])
			try:
				self.open_socket(host, port)
			except socket.gaierror:
				print('WARNING: no service listening on %s:%d' % (host, port,))
				error_happened = True
			if error_happened:
				print('There was an error. Too bad.')
			else:
				print('There was no errors. Good.')


if __name__ == '__main__':
	"""
	the main invocation point.
	"""
	checker = Checker()
	checker.check_with_config_yaml()

