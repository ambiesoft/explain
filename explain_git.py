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
    
        
def explain_git_status(commands):
    print('git-status - Show the working tree status')
    for arg in commands:
        if False:
            pass
        elif arg in ['-v', '--verbose']:
            printcmd(arg, 'be verbose')
        
def explain_git(commands):
    ''' explain '''
    
    print('git - the stupid content tracker')    
    if commands[0] == 'git':
        commands.pop(0)
    
    for prev,arg,next in neighborhood(commands):
        # print prev, item, next    
        # for arg in commands:
        if False:
            pass
        elif arg in ['--version']:
            printcmd(arg,'Prints the Git suite version that the git program came from.')
        elif arg in ['--help']:
            printcmd(arg,''' Prints the synopsis and a list of the most commonly used commands.
           If the option --all or -a is given then all available commands are
           printed. If a Git command is named this option will bring up the
           manual page for that command.''')
        elif arg in ['-C']:
            printcmd(arg,'''Run as if git was started in "{0}" instead of the current working
           directory. When multiple -C options are given, each subsequent
           non-absolute -C <path> is interpreted relative to the preceding -C
           <path>.'''.format(next))
        elif arg in ['-c']:
            printcmd(arg,'''Pass a configuration parameter to the command. The value given will
           override values from configuration files. The <name> is expected in
           the same format as listed by git config (subkeys separated by
           dots).'''.format(next))

        elif arg.startswith('-'):
            printcmd(arg, 'Unknown')
            
        else:
            # subcommand
            subCommands = []
            
            # take all following args
            for _,subarg,_ in neighborhood(commands):
                subCommands.append(subarg)
            
            explain_git_status(subCommands)
            return
            
            
        
            
        
def printLine():
    print('-' * 70)
    
if __name__ == '__main__':
    explain_git('git -C out/debug status -v'.split())
    printLine()
    explain_git('git status -v'.split())
    printLine()
