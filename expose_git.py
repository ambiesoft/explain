#!/usr/bin/env python3
from _ast import arg

def printcmd(arg, explanation):
    print('{}: {}'.format(arg,explanation))
    
def neighborhood(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)
    
        
def expose_git_status(commands):
    print('git-status - Show the working tree status')
    for arg in commands:
        if False:
            pass
        elif arg in ['-v', '--verbose']:
            printcmd(arg, '''
  In addition to the names of files that have been changed, also show
  the textual changes that are staged to be committed (i.e., like the
  output of git diff --cached). If -v is specified twice, then also
  show the changes in the working tree that have not yet been staged
  (i.e., like the output of git diff).
            ''')
        elif arg in ['-s', '--short']:
            printcmd(arg, '''
  Give the output in the short-format.
            ''')
        elif arg in ['-b', '--branch']:
            printcmd(arg, '''
  Show the branch and tracking info even in short-format.
            ''')
        elif arg in ['--show-stash']:
            printcmd(arg, '''
  Show the number of entries currently stashed away.
            ''')
        elif arg.startswith('--porcelain'):
            printcmd(arg, '''
  Give the output in an easy-to-parse format for scripts. This is
  similar to the short output, but will remain stable across Git
  versions and regardless of user configuration. See below for
  details.
            ''')
        elif arg in ['--long']:
            printcmd(arg, '''
  Give the output in the long-format. This is the default.
            ''')
        
def expose_git(commands):
    ''' expose '''
    
    print('git - the stupid content tracker')    
    if commands[0] == 'git':
        commands.pop(0)
    
    skip = 0
    subCommands = []
    enterSub = False
    for prev,arg,next in neighborhood(commands):
        # print prev, item, next    
        # for arg in commands:
        if enterSub:
            # take all following args
            #for _,subarg,_ in neighborhood(commands):
            #    subCommands.append(subarg)
            subCommands.append(arg)
            continue

        if skip != 0:
          skip -= 1
          continue
        
        if False:
            pass
        elif arg in ['--version']:
            printcmd(arg,'''
  Prints the Git suite version that the git program came from.
            ''')
        elif arg in ['--help']:
            printcmd(arg,'''
  Prints the synopsis and a list of the most commonly used commands.
  If the option --all or -a is given then all available commands are
  printed. If a Git command is named this option will bring up the
  manual page for that command.
           ''')
        elif arg in ['-C']:
            printcmd(arg + ' ' + next,'''
  Run as if git was started in "{0}" instead of the current working
  directory. When multiple -C options are given, each subsequent
  non-absolute -C <path> is interpreted relative to the preceding -C
  <path>.
            '''.format(next))
            skip=1
        elif arg in ['-c']:
            printcmd(arg + ' ' + next, '''
  Pass a configuration parameter to the command. The value given will
  override values from configuration files. The "{0}" is expected in
  the same format as listed by git config (subkeys separated by
  dots).
            '''.format(next.split('=')[0]))
            skip=1

        elif arg.startswith('-'):
            printcmd(arg, 'Unknown')
            
        else:
            # subcommand
            enterSub = True

    if subCommands:
      expose_git_status(subCommands)
      

            
        
            
        
def printLine():
    print('-' * 70)
    
if __name__ == '__main__':
    expose_git('git -C out/debug -c aaabbb=12345 status -v --porcelain'.split())
    printLine()
    expose_git('git status -v'.split())
    printLine()
