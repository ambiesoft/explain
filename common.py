

VALIDCOMMANDCHARS = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' 
def isValidCommand(command):
    '''
    '''
    if set(VALIDCOMMANDCHARS) < set(command):
        return False
    return True

def getInvalidCommandNameErrorString():
    '''
    '''
    return _('Command name must be a combination of "{0}"').format(VALIDCOMMANDCHARS)

def neighborhood(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)
    
EXPINDENT = '    '
def printcmd(arg, explanation):
    print('{}:'.format(arg))
    for line in explanation.strip().splitlines():
        print(EXPINDENT + line.strip())    