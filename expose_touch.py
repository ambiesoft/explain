#!/usr/bin/env python3
from _ast import arg

def printcmd(arg, explanation):
    print('{}: {}'.format(arg,explanation))
    
def expose_touch(commands):
    ''' touch '''
    
    print('touch - change file timestamps')    
    if commands[0] == 'touch':
        commands.pop(0)
    
    i = 0
    count = len(commands)
    while i < count:
      arg = commands[i]
      if False:
        pass
      elif arg in ['-a']:
        printcmd(arg,'''
  change only the access time
        ''')
      elif arg in ['-c', '--no-create']:
        printcmd(arg,'''
  do not create any files
        ''')
            
      i += 1  
            
        
            
        
def printLine():
    print('-' * 70)
    
if __name__ == '__main__':
    expose_touch('touch -a -c'.split())
    printLine()
