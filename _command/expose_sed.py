#!/usr/bin/env python3
from _ast import arg
from _operator import sub
from createExpose import errorExit
from common import printcmd,neighborhood

    

def inList(arg, next, argstring):
    l = argstring.split(",")
    return arg in [s.strip() for s in l]

        
def expose_sed(commands):
    ''' expose '''
    
    print('sed - stream editor for filtering and transforming text')    
    if len(commands)==0:
        return
    if commands[0] == 'git':
        commands.pop(0)
    
    skip = 0
    subCommands = []
    subCommand = ''
    for prev,arg,next in neighborhood(commands):

        if skip != 0:
            skip -= 1
            continue
        
        if False:
            pass
        elif inList(arg, next, "-n, --quiet, --silent"):
            printcmd(arg,'''suppress automatic printing of pattern space''')
        elif inList(arg, next, "--debug"):
            printcmd(arg, 'annotate program execution')
            
        
