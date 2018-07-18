#!/usr/bin/env python3
from argparse import ArgumentParser
from common import isValidCommand, getInvalidCommandNameErrorString
import os

def _(s):
    return s

def errorExit(message):
    print(message)
    exit(1)

def main():
    '''
    Create expose
    '''

    parser = ArgumentParser(prog='createExpose', 
                            description='Create expose command')
    
    parser.add_argument('command', nargs='+')
    
    commandline = parser.parse_args().command
    

    if not commandline:
        errorExit(_('No command')) 
                            
    prog = '_'.join(commandline)
    
    if not isValidCommand(prog):
        errorExit(getInvalidCommandNameErrorString())
        
    thisDir = os.path.dirname(os.path.realpath(__file__))
    expose_prog_py = os.path.join(thisDir, 'expose_{}.py'.format(prog))
    if os.path.exists(expose_prog_py):
        errorExit(_('"{0}" already exists').format(expose_prog_py))
    
    lines = []
    with open('sampletroff/strace.1') as f:
        lines = f.readlines()
    
    nameIndex = lines.index('.SH NAME')
    name = lines[nameIndex+1]
    
    
    
    
            
                          





if __name__ == '__main__':
    main()
