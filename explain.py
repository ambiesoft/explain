#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
from importlib import import_module
from importlib.machinery import SourceFileLoader

def processGit(commands):
	if not commands:
		errorExit(mi('No options or arguments'))
	

def processLs(commands):
	''' ls '''
	


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
	
	### load module from current directory, named 'explain_{commnad}' 
	commandModule = SourceFileLoader(moduleName, './' + moduleName + '.py').load_module()
	func = getattr(commandModule, moduleName)
	func(commands)

	# --- could not load only from current directory
	# __import__(moduleFile)
	# commandModule = sys.modules[moduleFile]
	# commandModule = import_module(moduleName)
	# func = getattr(commandModule, moduleName)
	# func(commands)
	
	
	
#https://stackoverflow.com/q/899276	
import csv
def split_quote(string,quotechar='"'):
    '''

    >>> split_quote('--blah "Some argument" here')
    ['--blah', 'Some argument', 'here']

    >>> split_quote("--blah 'Some argument' here", quotechar="'")
    ['--blah', 'Some argument', 'here']
    '''
    s = csv.StringIO(string)
    C = csv.reader(s, delimiter=" ",quotechar=quotechar)
    return list(C)[0]
   	

	   	
def main():
	'''
	explain
	'''
	
	inList = []
	if not sys.stdin.isatty():
		inList = sys.argv
	else:
   		inList = split_quote(sys.stdin.readline())
    
	if not inList:
		errorExit(mi('No commands specified'))
    	    
	
	processCommand(inList[1:])








if __name__ == '__main__':
	main()
