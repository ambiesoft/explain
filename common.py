

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