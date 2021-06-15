#!/usr/bin/env python3
from _ast import arg
from _operator import sub
from createExpose import errorExit
from common import printcmd,neighborhood

def expose_git_checkout(commands):
    print('git-checkout - Switch branches or restore working tree files')
    
    skip = 0

    # for arg in commands:
    for prev,arg,next in neighborhood(commands):    
        
        if skip != 0:
            skip -= 1
            continue
        
        if False:
            pass
        elif arg in ['-q', '--quiet']:
            printcmd(arg, '''
    Quiet, suppress feedback messages.
            ''')
        elif arg in ['--progress', '--no-progress']:
            printcmd(arg, '''
Progress status is reported on the standard error stream by default
when it is attached to a terminal, unless --quiet is specified.
This flag enables progress reporting even if not attached to a
terminal, regardless of --quiet.
              ''')
        elif arg in ['-f', '--force']:
            printcmd(arg, '''
When switching branches, proceed even if the index or the working
tree differs from HEAD. This is used to throw away local changes.

When checking out paths from the index, do not fail upon unmerged
entries; instead, unmerged entries are ignored.
            ''')
        elif arg in ['--ours', '--theirs']:
            printcmd(arg, '''
When checking out paths from the index, check out stage #2 (ours)
or #3 (theirs) for unmerged paths.

Note that during git rebase and git pull --rebase, ours and theirs
may appear swapped; --ours gives the version from the branch the
changes are rebased onto, while --theirs gives the version from the
branch that holds your work that is being rebased.
            ''')
        elif arg in ['-b']:
            printcmd(arg + ' ' + next, '''
    Create a new branch named {0} and start it at
    <start_point>; see git-branch(1) for details.
            '''.format(next))
            skip=1            
        elif arg in ['-t', '--track']:
            printcmd(arg, '''
When creating a new branch, set up "upstream" configuration. See
"--track" in git-branch(1) for details.

If no -b option is given, the name of the new branch will be
derived from the remote-tracking branch, by looking at the local
part of the refspec configured for the corresponding remote, and
then stripping the initial part up to the "*". This would tell us
to use "hack" as the local branch when branching off of
"origin/hack" (or "remotes/origin/hack", or even
"refs/remotes/origin/hack"). If the given name has no slash, or the
above guessing results in an empty name, the guessing is aborted.
You can explicitly give a name with -b in such a case.
            ''')

def expose_git_clean(commands):
    print('git-clean - Remove untracked files from the working tree')
    if len(commands)==0:
        return
    expose_git_clean2(commands)

def expose_git_clean2(commands):
    skip = 0
    for prev,arg,next in neighborhood(commands):  
        if skip != 0:
            skip -= 1
            continue
        if False:
            pass
        elif arg in ['-d']:
            printcmd(arg, '''
Normally, when no <path> is specified, git clean will not recurse into
untracked directories to avoid removing too much. Specify -d to have it
recurse into such directories as well. If any paths are specified, -d is
irrelevant; all untracked files matching the specified paths (with
exceptions for nested git directories mentioned under --force) will be
removed.
            ''')
        elif arg in ['-f', '--force']:
            printcmd(arg,'''
If the Git configuration variable clean.requireForce is not set to false,
git clean will refuse to delete files or directories unless given -f or -i.
Git will refuse to modify untracked nested git repositories (directories
with a .git subdirectory) unless a second -f is given.
            ''')
        elif arg in ['-i', '--interactive']:
            printcmd(arg,'''
    Show what would be done and clean files interactively. See “Interactive
    mode” for details.
            ''')
        elif arg in ['-n', '--dry-run']:
            printcmd(arg,'''
    Don’t actually remove anything, just show what would be done.
            ''')
        elif arg in ['-q', '--quiet']:
            printcmd(arg,''')
           Be quiet, only report errors, but not the files that are successfully
           removed.
           ''')
        elif arg=='-e' or arg.startswith('--exclude='):
            if arg=='-e':
                pattern = next;
                skip = 1
            else:
                pattern = arg[len('--exclude='):]
            printcmd(arg,'''
           Use the given exclude pattern in addition to the standard ignore rules (see
           gitignore(5)).
           ''')
        elif arg in ['-x']:
            printcmd(arg, '''
           Don’t use the standard ignore rules (see gitignore(5)), but still use the
           ignore rules given with -e options from the command line. This allows
           removing all untracked files, including build products. This can be used
           (possibly in conjunction with git restore or git reset) to create a pristine
           working directory to test a clean build.
            ''')
        elif arg in ['-X']:
            printcmd(arg, '''
           Remove only files ignored by Git. This may be useful to rebuild everything
           from scratch, but keep manually created files.
           ''')
        # compressed options
        elif arg.startswith('-'):
            if len(arg)==2:
                printcmd(arg, 'Unknown or too new or error')
            else:
                # Separate and add '-' for example,
                # '-df' becomes ['-d', '-f']
                expose_git_clean2(['-' + c for c in arg[1:]])
                

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
    if len(commands)==0:
        return
    if commands[0] == 'git':
        commands.pop(0)
    
    skip = 0
    subCommands = []
    subCommand = ''
    for prev,arg,next in neighborhood(commands):
        # print prev, item, next    
        # for arg in commands:
        if subCommand:
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
            subCommand = arg

    if subCommand:
        funcname = 'expose_git_{}'.format(subCommand)
        if funcname not in globals():
            errorExit('function {} not found'.format(funcname))
             
        func = globals()[funcname]

        func(subCommands)
        
      

            
        
            
        
def printLine():
    print('-' * 70)
    
if __name__ == '__main__':
    expose_git('git -C out/debug -c aaabbb=12345 status -v --porcelain'.split())
    printLine()
    expose_git('git status -v'.split())
    printLine()
