import builtins

def get_settings(n=9):  # This code will get settings, if there are exception(s), it will reset everything
        try:
            with open('PrintWithColor.settings', 'r') as settings:
                AllSettings = settings.read()
                settings.close()
                if AllSettings == '':
                    raise Exception
        except:
            with open('PrintWithColor.settings', 'w') as settings:
                AllSettings = ('False\nWHITE\nBLACK\nNORMAL\nWHITE\nBLACK\nNORMAL\nFalse')
                #                 1      2      3      4       5      6      7       8
                # 1       : DoNotResetColor
                # 2 --> 4 : DefaultForegroundColor, DefaultBackgroundColor, DefaultStyle
                # 5 --> 7 : LastForegroundColor   , LastBackgroundColor,    LastStyle
                # 8       : ForceDisableColoramaProxyObject
                settings.write(AllSettings)
                settings.close()

        AllSettings = AllSettings.split('\n')
        if AllSettings[0] == "True":
            AllSettings[0] = True
        else:
            AllSettings[0] = False
        if AllSettings[7] == "True":
            AllSettings[7] = True
        else:
            AllSettings[7] = False

        if n < 8:
            return AllSettings[n-1]
        else:
            return AllSettings


def set_settings(n, value):     # <--  print.change_settngs

    AllSettings = get_settings()
    # 1       : DoNotResetColor
    # 2 --> 4 : DefaultForegroundColor, DefaultBackgroundColor, DefaultStyle
    # 5 --> 7 : LastForegroundColor   , LastBackgroundColor,    LastStyle

    with open('PrintWithColor.settings', 'w') as settings:
        AllSettings[n-1] = value
        if AllSettings[0] == True:
            AllSettings[0] = "True"
        else:
            AllSettings[0] = "False"
        if AllSettings[7] == True:
            AllSettings[7] = "True"
        else:
            AllSettings[7] = "False"
        
        settings.write('\n'.join( [str(i) for i in AllSettings] ))
        settings.close()

def printToComputer(self, *textfrominput, sep = ' ', end = '\n', file = None, flush = False, fore, back, forestyle,):

    # Đoạn code này dùng để hiển thị chữ có màu trên Windows

    import os
    os.system("")

    from colorama import Fore        as FORE  # <-- Foreground Colors
    from colorama import Back        as BACK  # <-- Background Colors
    from colorama import Style       as STYLE # <-- Style
    from colorama import init        as __init
    from colorama import AnsiToWin32 as __AnsiToWin32
    import sys
    __init(wrap=False)
    __stream = __AnsiToWin32(sys.stderr).stream

    # Từ điển màu chữ
    foreground_dict = {
        # Normal colors
        "WHITE"     : FORE.WHITE,
        "RED"       : FORE.RED,
        "GREEN"     : FORE.GREEN,
        "YELLOW"    : FORE.YELLOW,
        "BLUE"      : FORE.BLUE,
        "MAGENTA"   : FORE.MAGENTA,
        "CYAN"      : FORE.CYAN,
        "BLACK"     : FORE.BLACK,
        # Dim colors
        "D WHITE"   : STYLE.DIM + FORE.WHITE,
        "D RED"     : STYLE.DIM + FORE.RED,
        "D GREEN"   : STYLE.DIM + FORE.GREEN,
        "D YELLOW"  : STYLE.DIM + FORE.YELLOW,
        "D BLUE"    : STYLE.DIM + FORE.BLUE,
        "D MAGENTA" : STYLE.DIM + FORE.MAGENTA,
        "D CYAN"    : STYLE.DIM + FORE.CYAN,
        "D BLACK"   : STYLE.DIM + FORE.BLACK,

        # Normal colors
        "B WHITE"   : STYLE.BRIGHT + FORE.WHITE,
        "B RED"     : STYLE.BRIGHT + FORE.RED,
        "B GREEN"   : STYLE.BRIGHT + FORE.GREEN,
        "B YELLOW"  : STYLE.BRIGHT + FORE.YELLOW,
        "B BLUE"    : STYLE.BRIGHT + FORE.BLUE,
        "B MAGENTA" : STYLE.BRIGHT + FORE.MAGENTA,
        "B CYAN"    : STYLE.BRIGHT + FORE.CYAN,
        "B BLACK"   : STYLE.BRIGHT + FORE.BLACK,
    }

    background_dict = {
        "WHITE"  : BACK.WHITE,
        "RED"    : BACK.RED,
        "GREEN"  : BACK.GREEN,
        "YELLOW" : BACK.YELLOW,
        "BLUE"   : BACK.BLUE,
        "MAGENTA": BACK.MAGENTA,
        "CYAN"   : BACK.CYAN,
        "BLACK"  : BACK.BLACK,
    }

    styles_dict = {
        "BOLD"      : "\u001b[1m",
        "UNDERLINE" : "\u001b[4m",
        "REVERSED"  : "\u001b[7m",
        "NORMAL"    : STYLE.NORMAL,
        "BRIGHT"    : STYLE.BRIGHT,
        "DIM"       : STYLE.DIM,
    }

    # This list will contain all acceptable colors
    LegitColors1 = [
        'WHITE','RED','GREEN','YELLOW','BLUE','MAGENTA','CYAN','BLACK',
        'D WHITE','D RED','D GREEN','D YELLOW','D BLUE','D MAGENTA','D CYAN','D BLACK',
        'B WHITE','B RED','B GREEN','B YELLOW','B BLUE','B MAGENTA','B CYAN','B BLACK'
        ]

    LegitColors2 = ['WHITE','RED','GREEN','YELLOW','BLUE','MAGENTA','CYAN','BLACK', "DIM", "NORMAL", "BRIGHT"]


    fore = fore.upper()
    back = back.upper()
    forestyle = forestyle.upper()


    # Search in 3 dictionaries
    try:
        ss = styles_dict[forestyle]

        # Check colors, if value is between from 0 to 255 --> using 8-bit ANSI colors
        # if not, using 4-bit ANSI colors with Colorama's proxy object

        if fore in LegitColors1:
            ff = foreground_dict[fore]
        elif int(fore) in range(0, 256):
            fore = str(fore)
            ff = f"\u001b[38;5;{fore}m"
        else:
            raise Exception

        if back in LegitColors2:
            bb = background_dict[back]
        elif int(back) in range(0, 256):
            back = str(back)
            bb = f"\u001b[48;5;{back}m"
        else:
            raise Exception
    
    except:                             # If errors, reset 3 colors into default and check errors
        ff = foreground_dict['WHITE']
        bb = background_dict['BLACK']
        ss = styles_dict['NORMAL']


        if fore == get_settings(2) or fore not in LegitColors1:
      # if fore == DefaultForegroundColor or fore == LastForegroundColor or fore not in LegitColors:
            set_settings(2, 'WHITE')
        elif fore == get_settings(5):
      # elif fore == LastForegroundColor:
            set_settings(5, 'WHITE')
        
        if back == get_settings(3) or back not in LegitColors2:
      # if back == DefaultBackgroundColor or back == LastBackgroundColor or back not in LegitColors:
            set_settings(3, 'BLACK')
        elif back == get_settings(6):
      # elif fore == LastForegroundColor:
            set_settings(6, 'BLACK')
        
        if forestyle == get_settings(4) or forestyle not in ['BOLD','ITALIC','RESERVED', 'NORMAL', 'BRIGHT', 'DIM']:
            set_settings(4, 'NORMAL')
      # elif fore == LastForegroundColor:
        elif forestyle == get_settings(7):
            set_settings(7, 'NORMAL')

        if get_settings(1) not in [True, False]:
            set_settings(1, False)

    global fileIsWriteable

    try:    # Check if file argument is a writeable file?
            # If it is a writeable file, write the output to it
        if file != None:
            file.write('')
            fileIsWriteable = True
        else:
            fileIsWriteable = False
    except:
        fileIsWriteable = False

    ForceDisableColoramaProxyObject = get_settings(8)

    for item in textfrominput:
        if item != textfrominput[-1]:
            if not fileIsWriteable:
                if int(fore) in range(0, 256) or int(back) in range(0, 256) or ForceDisableColoramaProxyObject or forestyle in ['BOLD','ITALIC','RESERVED', 'NORMAL', 'BRIGHT', 'DIM']:
                    builtins.print(ff+bb+ss+item, end=sep, flush=flush, file=file)
                else:
                    builtins.print(ff+bb+ss+item, end=sep, flush=flush, file=__stream)
            else:
                file.write(item+sep)

        else:
            if not fileIsWriteable:
                if str(fore).isnumeric():
                    if int(fore) in range(0, 256) or int(back) in range(0, 256) or ForceDisableColoramaProxyObject or forestyle in ['BOLD','ITALIC','RESERVED', 'NORMAL', 'BRIGHT', 'DIM']:
                        builtins.print(ff+bb+ss+item, end=end, flush=flush, file=file)
                        print("it's Okay")
                    else:
                        builtins.print(ff+bb+ss+item, end=end, flush=flush, file=__stream)
                else:
                    builtins.print(ff+bb+ss+item, end=end, flush=flush, file=__stream)
            else:
                file.write(item+end)
        
    if get_settings(1)== False:  # if DoNotResetColor == False:
        builtins.print(STYLE.RESET_ALL, end='')
        # LastForegroundColor = DefaultForegroundColor
        set_settings(5, get_settings(2))
        # LastBackgroundColor = DefaultBackgroundColor
        set_settings(6, get_settings(3))
        # LastStyle = DefaultStyle
        set_settings(7, get_settings(4))

        print("\u001b[0m")
    else:
        # LastBackgroundColor = back
        # LastForegroundColor = fore
        # LastStyle = forestyle

        set_settings(5, fore)
        set_settings(6, back)
        set_settings(7, forestyle)

    try:
        file.close()
    except:
        pass

get_settings()