#!/usr/bin/env python3

import sys
# from argparse import ArgumentParser
# from importlib import import_module
from importlib.machinery import SourceFileLoader
from common import isValidCommand


def myp(m):
    print(m)
    
def errorExit(m):
    myp(m)
    exit(1)

def processCommand(commands):
    command = commands.pop(0)
#    if not command in availableCommands.key():
#        errorExit(mi('%1 is not yet ready').format(command))

    #
    # import a file and call, in case of 'ls', module file name will be 'expose-ls.py'
    #
    
    # check command is valid
    if not isValidCommand(command):
        errorExit(_('"{}" contains invalid character').format(command))


    moduleName = 'expose_' + command
    
    ### load module from current directory, named 'expose_{commnad}' 
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
    expose
    '''
    
    
    inList = []
    if not sys.stdin.isatty():
        inList = sys.argv
    else:
        inList = split_quote(sys.stdin.readline())
    
    if not inList:
        errorExit(_('No commands specified'))
            
    
    processCommand(inList[1:])








if __name__ == '__main__':
    main()
