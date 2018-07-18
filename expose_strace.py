#!/usr/bin/env python3
from _ast import arg

def printcmd(arg, explanation):
    print('{}: {}'.format(arg,explanation))
    
def expose_strace(commands):
    ''' touch '''
    
    print('strace - trace system calls and signals')    
    if commands[0] == 'strace':
        commands.pop(0)
    
    i = 0
    count = len(commands)
    while i < count:
        arg = commands[i]
        if False:
            pass
        elif arg in ['-c']:
            printcmd(arg,'''
    Count time, calls, and errors  for  each  system  call  and
    report  a summary on program exit.  On Linux, this attempts
    to show system time (CPU time spent running in the  kernel)
    independent  of  wall clock time.  If -c is used with -f or
    -F (below), only aggregate totals for all traced  processes
    are kept.
            ''')
        elif arg in ['-C']:
            printcmd(arg,'''
    Like  -c  but also print regular output while processes are
    running.
            ''')
        elif arg in ['-D']:
            printcmd(arg,'''
    Run tracer process as a detached grandchild, not as  parent
    of  the  tracee.  This reduces the visible effect of strace
    by keeping  the  tracee  a  direct  child  of  the  calling
    process.
            ''')
        elif arg in ['-d']:
            printcmd(arg,'''
    Show some debugging output of strace itself on the standard
    error.
            ''')
        elif arg in ['-f']:
            printcmd(arg,'''
    Trace child processes as  they  are  created  by  currently
    traced  processes  as a result of the fork(2), vfork(2) and
    clone(2) system calls.  Note that -p PID -f will attach all
    threads  of  process  PID if it is multi-threaded, not only
    thread with thread_id = PID.
            ''')
        elif arg in ['-ff']:
            printcmd(arg,'''
    If the -o filename option  is  in  effect,  each  processes
    trace  is  written to filename.pid where pid is the numeric
    process id of each process.  This is incompatible with  -c,
    since no per-process counts are kept.
            ''')
        elif arg in ['-h']:
            printcmd(arg,'''
        Print the help summary.
            ''')
        elif arg in ['-i']:
            printcmd(arg,'''
    Print the instruction pointer at the  time  of  the  system
    call.
            ''')
        elif arg in ['-k']:
            printcmd(arg,'''
    Print  the  execution  stack  trace of the traced processes
    after each system  call  (experimental).   This  option  is
    available only if strace is built with libunwind.
            ''')
        elif arg in ['-q']:
            printcmd(arg,'''
    Suppress  messages  about  attaching,  detaching etc.  This
    happens automatically when output is redirected to  a  file
    and the command is run directly instead of attaching.
            ''')
        elif arg in ['-qq']:
            printcmd(arg,'''
    If  given  twice, suppress messages about process exit sta‐
    tus.
            ''')
            
        i += 1  
            
        
            
        
def printLine():
    print('-' * 70)
    
if __name__ == '__main__':
    expose_strace('strace -p 12345'.split())
    printLine()
