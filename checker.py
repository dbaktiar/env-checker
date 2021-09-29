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
import urllib
import yaml


class Checker(object):
	"""
	Checker class.
	"""

	def __init__(self, config_yaml='default.yaml'):
		"""
		Initialize the class Checker.
		"""
		print('reading yaml config file [%s]...' % (config_yaml,))
		with open(config_yaml) as yaml_file:
			self._config_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)

	def open_socket(self, host, port):
		"""
		Open and check if there is a listening socket in the (host, port)
		"""
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print('connecting to %s:%d...' % (host, port,))
		s.connect((host, port,))
		s.close()
		print('done.')

	def open_http(self, url_base, context_path, params):
		"""
		perform deeper check by invoking the http/https endpoints
		with some predefined parameters.
		this will catch http errors and reports it.
		"""
		url = '%s%s' % (url_base, context_path,)
		print('opening url [%s]' % (url,))
		f = urllib.request.urlopen(url)
		print(f.read(1000))
		print('done.')

	def check_services(self):
		"""
		perform the check
		"""
		for service in self._config_yaml['services-check']:
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

	def check_endpoints(self):
		"""
		perform the check
		"""
		checklist = self._config_yaml['endpoints-check'] 
		print(checklist)
		for entry in checklist:
			print('checking endpoints [%s]...' % (entry['name']))
			error_happened = False
			service_name = entry['service-name']
			endpoint = entry['endpoint'] 
			try:
				self.open_http(host, port)
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
	# checker.check_services()
	checker.check_endpoints()


