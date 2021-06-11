#!/usr/bin/env python3
from _ast import arg

def printcmd(arg, explanation):
    print('{}: {}'.format(arg,explanation))
    
def expose_ls(commands):
    ''' expose '''
    
    print('ls: list files and directories')    
    if len(commands)==0:
        return
    if commands[0] == 'ls':
        commands.pop(0)
    
    for arg in commands:
        if arg in ['-a','--all']:
            printcmd(arg,'''
  do not ignore entries starting with .
            ''')
        elif arg=='-A' or arg=='--almost-all':
            printcmd(arg, '''
  do not list implied . and ..
            ''')
        elif arg=='--author':
            printcmd(arg, '''
  with -l, print the author of each file
            ''')
        elif arg=='-b' or arg=='--escape':
            printcmd(arg, '''
            print C-style escapes for nongraphic characters
            ''')
        elif arg.startswith('--block-size='):
            printcmd(arg, '''
  scale   sizes   by   SIZE   before   printing    them.     E.g.,
  '--block-size=M'  prints sizes in units of 1,048,576 bytes.  See
  SIZE format below.
            ''')
        elif arg in ['-B', '--ignore-backups']:
            printcmd(arg, '''
  do not list implied entries ending with ~
            ''')
        elif arg=='-c':
            printcmd(arg, '''
  with -lt: sort by, and show, ctime (time of last modification of
  file  status  information)  with -l: show ctime and sort by name
  otherwise: sort by ctime, newest first
              ''')
        elif arg=='-C':
            printcmd(arg, '''
  list entries by columns
            ''')
        elif arg.startswith('--color'):
            printcmd(arg, '''
  colorize the output.   WHEN  defaults  to  'always'  or  can  be
  'never' or 'auto'.  More info below
              ''')
        elif arg in ['-d','--directory']:
            printcmd(arg, '''
  list  directory entries instead of contents, and do not derefer-
  ence symbolic links
            ''')
        elif arg in ['-D','--dired']:
            printcmd(arg, '''
  generate output designed for Emacs' dired mode
            ''')
        elif arg=='-f':
            printcmd(arg, '''
  do not sort, enable -aU, disable -ls --color
            ''')
        elif arg in ['-F', '--classify']:
            printcmd(arg, '''
  append indicator (one of */=>@|) to entries
            ''')
        elif arg=='--file-type':
            printcmd(arg, """
  likewise, except do not append '*'
            """)
        elif arg.startswith('--format'):
            printcmd(arg, '''
  across -x, commas -m, horizontal -x, long -l, single-column  -1,
  verbose -l, vertical -C
            ''')
        elif arg=='--full-time':
            printcmd(arg, '''
  like -l --time-style=full-iso
            ''')
        elif arg=='-g':
            printcmd(arg, '''
  like -l, but do not list owner
            ''')
        elif arg=='--group-directories-first':
            printcmd(arg,'''
  group directories before files.
  
  augment  with  a  --sort option, but any use of --sort=none (-U)
  disables grouping
            ''')
        elif arg in ['-G', '--no-group']:
            printcmd(arg,'''
  in a long listing, don't print group names
            ''')
        elif arg in ['-h', '--human-readable']:
            printcmd(arg, '''
  with -l, print sizes in human readable format (e.g., 1K 234M 2G)
            ''')
        elif arg=='--si':
            printcmd(arg, '''
  likewise (as -h), but use powers of 1000 not 1024
            ''')
        elif arg in ['-H', '--dereference-command-line']:
            printcmd(arg, '''
  follow symbolic links listed on the command line
            ''')
        elif arg=='--dereference-command-line-symlink-to-dir':
            printcmd(arg, '''
  follow each command line symbolic link that points to  a  direc-
  tory
            ''')
        elif arg.startswith('--hide='):
            printcmd(arg, '''
  do  not  list implied entries matching shell PATTERN (overridden
  by -a or -A)
            ''')
        elif arg.startswith('--indicator-style='):
            printcmd(arg,'''
  append indicator with style WORD to entry names: none (default),
  slash (-p), file-type (--file-type), classify (-F)
            ''')
        elif arg in ['-i', '--inode']:
            printcmd(arg, '''
  print the index number of each file
            ''')
        elif arg=='-I' or arg.startswith('--ignore='):
            printcmd(arg, '''
  do not list implied entries matching shell PATTERN
            ''')
        elif arg in ['-k', '--kibibytes']:
            printcmd(arg, '''
  use 1024-byte blocks
            ''')
        elif arg=='-l':
            printcmd(arg, '''
  use a long listing format
            ''')
        elif arg in ['-L', '--dereference']:
            printcmd(arg, '''
  when showing file information for a symbolic link, show informa-
  tion for the file the link references rather than for  the  link
  itself
            ''')
        elif arg=='-m':
            printcmd(arg, '''
  fill width with a comma separated list of entries
            ''')
        elif arg in ['-n', '--numeric-uid-gid']:
            printcmd(arg, '''
  like -l, but list numeric user and group IDs
            ''')
        elif arg in ['-N', '--literal']:
            printcmd(arg, '''
  print  raw entry names (don't treat e.g. control characters spe-
  cially)
            ''')
        elif arg=='-o':
            printcmd(arg,'''
  like -l, but do not list group information
            ''')
        elif arg=='-p' or arg.startswith('--indicator-style='):
            printcmd(arg,'''
  append / indicator to directories
            ''')
        elif arg in ['-q', '--hide-control-chars']:
            printcmd(arg, '''
  print ? instead of non graphic characters
            ''')
        elif arg=='--show-control-chars':
            printcmd(arg,'''
  show non graphic characters as-is  (default  unless  program  is
  'ls' and output is a terminal)
            ''')
        elif arg in ['-Q', '--quote-name']:
            printcmd(arg, '''
  enclose entry names in double quotes
            ''')
        elif arg.startswith('--quoting-style='):
            printcmd(arg,'''
  use  quoting style WORD for entry names: literal, locale, shell,
  shell-always, c, escape
            ''')
        elif arg in ['-r', '--reverse']:
            printcmd(arg, '''
  reverse order while sorting
            ''')
        elif arg in ['-R', '--recursive']:
            printcmd(arg, '''
  list subdirectories recursively
            ''')
        elif arg in ['-s','--size']:
            printcmd(arg, '''
  print the allocated size of each file, in blocks
            ''')
        elif arg=='-S':
            printcmd(arg,'''
  sort by file size
            ''')
        elif arg.startswith('--sort='):
            printcmd(arg,'''
  sort by WORD instead of name: none -U, extension  -X,  size  -S,
  time -t, version -v
            ''')
        elif arg.startswith('--time='):
            printcmd(arg,'''
  with  -l,  show time as WORD instead of modification time: atime
  -u, access -u, use -u, ctime -c, or  status  -c;  use  specified
  time as sort key if --sort=time
            ''')
        elif arg.startswith('--time-style='):
            printcmd(arg,'''
  with  -l, show times using style STYLE: full-iso, long-iso, iso,
  locale, +FORMAT.  FORMAT is interpreted like 'date';  if  FORMAT
  is  FORMAT1<newline>FORMAT2, FORMAT1 applies to non-recent files
  and FORMAT2 to recent files; if STYLE is prefixed with 'posix-',
  STYLE takes effect only outside the POSIX locale
            ''')
        elif arg=='-t':
            printcmd(arg,'''
  sort by modification time, newest first
            ''')
        elif arg=='-T' or arg.startswith('--tabsize='):
            printcmd(arg,'''
  assume tab stops at each COLS instead of 8
            ''')
        elif arg=='-u':
            printcmd(arg,'''
  with  -lt:  sort  by, and show, access time with -l: show access
  time and sort by name otherwise: sort by access time
            ''')
        elif arg=='-U':
            printcmd(arg,'''
  do not sort; list entries in directory order
            ''')
        elif arg=='-v':
            printcmd(arg,'''
  natural sort of (version) numbers within text
            ''')
        elif arg=='-w' or arg.startswith('--width='):
            printcmd(arg,'''
  assume screen width instead of current value
            ''')
        elif arg=='-x':
            printcmd(arg,'''
  list entries by lines instead of by columns
            ''')
        elif arg=='-X':
            printcmd(arg,'''
  sort alphabetically by entry extension
            ''')
        elif arg in ['-Z', '--context']:
            printcmd(arg, '''
  print any SELinux security context of each file
            ''')
        elif arg=='-1':
            printcmd(arg,'''
  list one file per line
            ''')
        elif arg=='--help':
            printcmd(arg,'''
  display this help and exit
            ''')
        elif arg=='--version':
            printcmd(arg,'''
  output version information and exit
            ''')
            
            
            
            
            
            
            

            
            
            
  
        
             
        # 'ls' can have options like '-lAF', which means same as '-l -A -F'.
        elif arg.startswith('-'):
            if len(arg)==2:
                printcmd(arg, '''
  Unknown or too new or error
                ''')
            else:
                subarg = arg[1:]
                # Separate and add '-'
                message = '''
  same as "{}"
                '''.format('-' +  ' -'.join(list(subarg)))
                printcmd(arg, message)
                
        else:
            allmessage = '{0}'
            
            if arg=='.':
                message = '''
  current directory
                '''
            elif arg=='..':
                message = '''
  parent directory
                '''
            elif arg=='*':
                message = '''
  every file and directory, in case of directory, list content
  of the directory (not recursive unless '-R')
                '''
            elif arg.startswith('*'):
                message = '''
  every file and directory ends with '{}', in case of directory, 
  list content of the directory (not recursive unless '-R')
                '''.format(arg[1:])
            elif arg.endswith('*'):
                message = '''
  every file and directory starts with '{}', in case of directory, 
  list content of the directory (not recursive unless '-R')
                '''.format(arg[1:])
            elif '*' in arg:
                globArgs = arg.split('*')
                globLen = len(globArgs)
                if globLen==2:
                    message = '''
  every file and directory starts with '{}' and ends with '{}', 
  in case of directory, list content  of the directory (not 
  recursive unless '-R')
                    '''.format(globArgs[0], globArgs[1])
                else:
                    message = '''
  every files and directory satisfies the glob, in case of directory, 
  list content of the directory (not recursive unless '-R')
                    '''
            else:
                message = arg
                
            printcmd(arg, allmessage.format(message))
            
            
            
            
        
            
        
def printLine():
    print('-' * 70)
    
if __name__ == '__main__':
    expose_ls('ls -Fta --block-size=100 -V aaa bbb .'.split())
    printLine()
    expose_ls('ls *'.split())
    printLine()    
    expose_ls('ls aaa*'.split())
    printLine()    
    expose_ls('ls *bbb'.split())
    printLine()    
    expose_ls('ls -Fta xxx*yyy'.split())
    printLine()    
    expose_ls('ls -Fta xxx*yyy*zzz'.split())
    printLine()    
