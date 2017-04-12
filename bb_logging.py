#! python3

import logging
import config

class Logging (object):

	def __init__(self, module_name=None):
		self.logger = logging.getLogger(module_name)

	def info(self, s):
		self.logger.info(s)
		
	def warn(self, s):
		self.logger.warn(s)
		
	def error(self, s):
		self.logger.error(s)
			
	# Setup app logging
	def initiaize_logging(self, log_filename):
		'''
			Use this method only one time during application initialization
		'''
		self.logger.setLevel(logging.DEBUG)
		m = "a" if config.log_append == True else "w"
		self.fh =logging.FileHandler(log_filename, mode=m)
		self.fh.setLevel(logging.DEBUG)
		self.ch = logging.StreamHandler()
		self.ch.setLevel(logging.DEBUG)
		s = "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s"
		formatter = logging.Formatter(s)
		self.fh.setFormatter(formatter)
		self.ch.setFormatter(formatter)
		self.logger.addHandler(self.fh)
		self.logger.addHandler(self.ch)

	def stop(self):
		self.logger.removeHandler(self.fh)
		self.logger.removeHandler(self.ch)
		logging.shutdown()

	
 
