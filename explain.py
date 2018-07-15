#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
from importlib import import_module

def processGit(commands):
	if not commands:
		errorExit(mi('No options or arguments'))
	

def processLs(commands):
	''' ls '''
	

availableCommands = {
	'git': processGit, 
	'ls': processLs,
	}

def mi(m):
	''' I18N'''
	return m

def myp(m):
	print(m)
	
def errorExit(m):
	myp(m)
	exit(1)

def processCommand(commands):
	command = commands.pop(0)
#	if not command in availableCommands.key():
#		errorExit(mi('%1 is not yet ready').format(command))

	#
	# import a file and call, in case of 'ls', module file name will be 'explain-ls.py'
	#
	
	# check command is valid
	if set('-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') < set(command):
		errorExit(mi('"{}" contains invalid character').format(command))

	moduleName = 'explain_' + command
	# __import__(moduleFile)
	# commandModule = sys.modules[moduleFile]
	commandModule = import_module(moduleName)
	func = getattr(commandModule, moduleName)
	
	result = func(commands)
	
	
def main():
	'''
	explain
	'''
	
#	parser = ArgumentParser(
#		prog='explain', 
#		usage='explain command ...', 
#		description='shows the explanation of the command')
#		
#	parser.add_argument('command', help='any command')
#	args = parser.parse_args()

		
	command = sys.argv[1]
	if not command:
		errorExit(mi('No command specified'))
	
	processCommand(sys.argv[1:])








if __name__ == '__main__':
	main()
