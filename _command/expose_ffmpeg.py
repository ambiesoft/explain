#!/usr/bin/env python3
from _ast import arg
from common import printcmd,neighborhood
    
def expose_ffmpeg(commands):
    ''' expose '''
    
    print('ffmpeg - Hyper fast Audio and Video encoder')    
    if len(commands)==0:
        return
    expose_ffmpeg2(commands)

def expose_ffmpeg2(commands):
    if commands[0] == 'ffmpeg':
        commands.pop(0)
    
    skip = 0
    for prev,arg,next in neighborhood(commands):    
        if skip != 0:
            skip -= 1
            continue    

        if False:
            pass
        elif arg in ['-h', '-?', '--help']:
            if not next:
                printcmd(arg,'print basic options')
            elif next=='long':
                printcmd(arg, 'print more options')
            elif next=='full':
                printcmd(arg, ' print all options (including all format and codec specific options, very long)')
            else:
                printcmd(arg, 'show help')
        elif arg in ['-L']:
            printcmd(arg,'show license')
        elif arg in ['-version']:
            printcmd(arg, 'show version')
        elif arg =='-buildconf': printcmd(arg, 'show build configuration')
        elif arg =='-formats': printcmd(arg,'show available formats')
        elif arg =='-muxers': printcmd(arg,'show available muxers')
        elif arg =='-demuxers': printcmd(arg,'show available demuxers')
        elif arg =='-devices': printcmd(arg,'show available devices')
        elif arg =='-codecs': printcmd(arg,'show available codecs')
        elif arg =='-decoders': printcmd(arg,'show available decoders')
        elif arg =='-encoders': printcmd(arg,'show available encoders')
        elif arg =='-bsfs': printcmd(arg,'show available bit stream filters')
        elif arg =='-protocols': printcmd(arg,'show available protocols')
        elif arg =='-filters': printcmd(arg,'show available filters')
        elif arg =='-pix_fmts': printcmd(arg,'show available pixel formats')
        elif arg =='-layouts': printcmd(arg,'show standard channel layouts')
        elif arg =='-sample_fmts': printcmd(arg,'show available audio sample formats')
        elif arg =='-colors': printcmd(arg,'show available color names')
        elif arg =='-sources': 
            skip = 1
            printcmd(arg,'list sources of the input device')
        elif arg =='-sinks device':
            skip = 1
            printcmd(arg,'list sinks of the output device')
        elif arg =='-hwaccels': printcmd(arg,'show available HW acceleration methods')
            
        # TODO: Global options and more
            
            
