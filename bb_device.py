#coding: utf-8

from objc_util import *
import unicodedata

def get_current_device():
	UIDevice = ObjCClass('UIDevice')
	device=UIDevice.currentDevice()
	return device

def replace_right_quote(name):
	n = name.replace("\u2019", "\u0027")
	'''
	n = name
	for i, c in enumerate(name):
		if ord(c) == 2019:						# right quote char
			n[i]="'"
	'''
	return n
	
def print_name(name):
	for i,c in enumerate(name):
		print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
		print(unicodedata.name(c))
	
def get_device_name():
	device = get_current_device()
	name = str(device.name())
	return name

def get_safe_device_name():
	device = get_current_device()
	name = replace_right_quote(str(device.name()))
	return name
	
def main():
	name = get_device_name()
	print ("Device name: {}".format(name))
	print_name(name)
	n = replace_right_quote(name)
	print("Safe name: {}".format(n))
	print_name(n)
	
if __name__ == '__main__':
	main()
	

