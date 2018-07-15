

def printcmd(arg, explanation):
    print('{}: {}'.format(arg,explanation))
    
def explain_ls(commands):
    ''' explain '''
    
    
    if commands[0] == 'ls':
        print('ls: list files and directories')
        commands.pop(0)
    
    for arg in commands:
        if arg in ['-a','--all']:
            printcmd(arg,'do not ignore entries starting with .')
        elif arg=='-A' or arg=='--almost-all':
            printcmd(arg, 'do not list implied . and ..')
        elif arg=='--author':
            printcmd(arg, 'with -l, print the author of each file')
        elif arg=='-b' or arg=='--escape':
            printcmd(arg, 'print C-style escapes for nongraphic characters')
        elif arg.startswith('--block-size='):
            printcmd(arg, 
                     '''scale   sizes   by   SIZE   before   printing    them.     E.g.,
                     '--block-size=M'  prints sizes in units of 1,048,576 bytes.  See
                     SIZE format below.''')
        elif arg in ['-B', '--ignore-backups']:
            printcmd(arg, 'do not list implied entries ending with ~')
        elif arg=='-c':
            printcmd(arg, '''with -lt: sort by, and show, ctime (time of last modification of
              file  status  information)  with -l: show ctime and sort by name
              otherwise: sort by ctime, newest first''')
        elif arg=='-C':
            printcmd(arg, 'list entries by columns')
        elif arg.startswith('--color'):
            printcmd(arg, '''colorize the output.   WHEN  defaults  to  'always'  or  can  be
              'never' or 'auto'.  More info below''')
        elif arg in ['-d','--directory']:
            printcmd(arg, '''list  directory entries instead of contents, and do not derefer-
                          ence symbolic links''')
        elif arg in ['-D','--dired']:
            printcmd(arg, '''generate output designed for Emacs' dired mode''')
        elif arg=='-f':
            printcmd(arg, 'do not sort, enable -aU, disable -ls --color')
        elif arg in ['-F', '--classify']:
            printcmd(arg, ' append indicator (one of */=>@|) to entries')
        elif arg=='--file-type':
            printcmd(arg, "likewise, except do not append '*'")
        elif arg.startswith('--format'):
            printcmd(arg, '''across -x, commas -m, horizontal -x, long -l, single-column  -1,
              verbose -l, vertical -C''')
        elif arg=='--full-time':
            printcmd(arg, 'like -l --time-style=full-iso')
        elif arg=='-g':
            printcmd(arg, 'like -l, but do not list owner')
        elif arg=='--group-directories-first':
            printcmd(arg,'''group directories before files.

              augment  with  a  --sort option, but any use of --sort=none (-U)
              disables grouping''')
        elif arg in ['-G', '--no-group']:
            printcmd(arg,'''in a long listing, don't print group names''')
        elif arg in ['-h', '--human-readable']:
            printcmd(arg, '''with -l, print sizes in human readable format (e.g., 1K 234M 2G)''')
        elif arg=='--si':
            printcmd(arg, 'likewise (as -h), but use powers of 1000 not 1024')
        elif arg in ['-H', '--dereference-command-line']:
            printcmd(arg, 'follow symbolic links listed on the command line')
        elif arg=='--dereference-command-line-symlink-to-dir':
            printcmd(arg, """follow each command line symbolic link that points to  a  direc-
                          tory""")
        elif arg.startswith('--hide='):
            printcmd(arg, ''' do  not  list implied entries matching shell PATTERN (overridden
              by -a or -A)''')
        elif arg.startswith('--indicator-style='):
            printcmd(arg,'''append indicator with style WORD to entry names: none (default),
              slash (-p), file-type (--file-type), classify (-F)''')
        elif arg in ['-i', '--inode']:
            printcmd(arg, 'print the index number of each file')
        elif arg=='-I' or arg.startswith('--ignore='):
            printcmd(arg, 'do not list implied entries matching shell PATTERN')
        elif arg in ['-k', '--kibibytes']:
            printcmd(arg, 'use 1024-byte blocks')
        elif arg=='-l':
            printcmd(arg, 'use a long listing format')
        elif arg in ['-L', '--dereference']:
            printcmd(arg, '''when showing file information for a symbolic link, show informa-
                          tion for the file the link references rather than for  the  link
              itself''')
        elif arg=='-m':
            printcmd(arg, 'fill width with a comma separated list of entries')
        elif arg in ['-n', '--numeric-uid-gid']:
            printcmd(arg, 'like -l, but list numeric user and group IDs')
        elif arg in ['-N', '--literal']:
            printcmd(arg, '''print  raw entry names (don't treat e.g. control characters spe-
                                      cially)''')
        elif arg=='-o':
            printcmd(arg,'like -l, but do not list group information')
        
             
            
        elif arg.startswith('-'):
            subarg = arg[1:]
            # Separate and add '-'
            message = 'Same as {}'.format('-' +  ' -'.join(list(subarg)))
            printcmd(arg, message)
                
        else:
            printcmd(arg, 'list {}'.format(arg))
            
            
            
            
        
            
        

if __name__ == '__main__':
    explain_ls('ls -Fta --block-size=100 aaa bbb .'.split())    