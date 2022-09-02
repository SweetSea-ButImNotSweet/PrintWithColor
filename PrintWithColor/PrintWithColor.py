# Call builtins library, allow me to use the pure print command in Python
from PrintWithColor.PrintWithColorCore import *
# from PrintWithColorCore import *

# Sorry everyone, all this code still not translated into English :[

# Lệnh Printc là 
class print():
#   Note: sep, end, flush is added to simulate the print() syntax

#                                                                                                      s is style of foreground color <--|
#                                                                                                                                        |
#                                                                                        b is background color <--|                      |
#                                                                                                                 |                      |
#                                                                 f is foreground color <--|                      |                      |
#                                                                                          |                      |                      |
    def __init__ (self, *textfrominput, sep = ' ', end = '\n', file = None, flush = False, f = 'ForegroundColor', b = 'BackgroundColor', s = 'Style',):
#                                        |          |                         |--> flush: wipe all cache? (Default: False)
#                                        |          |
#                                        |          |==> end is ending character
#                                        |
#                                        |--> sep: seperate character between arguments
#
# For more infomation, visit: https://www.programiz.com/python-programming/methods/built-in/print
        
        # file argument handle files only! It will skip if file argument is not a writeabke file!
        # Reason: this wrapper is using colorama's proxy object!

        if f != 'ForegroundColor':
            set_settings(5, f)
        else:
            f = get_settings(5)

        if b != 'BackgroundColor':
            set_settings(6, b)
        else:
            b = get_settings(6)

        if s != 'Style':
            set_settings(7, s)
        else:
            s = get_settings(7)

        printToComputer(self, *textfrominput, sep = ' ', end = '\n', file = None, flush = False, fore = get_settings(5), back = get_settings(6), forestyle = get_settings(7),)

# get_settings(n) will return all these results based on n
# 1         : DoNotResetColor
# 2 > 3 > 4 : DefaultForegroundColor > DefaultBackgroundColor > DefaultStyle
# 5 > 6 > 7 : LastForegroundColor    > LastBackgroundColor    > LastStyle

    def change_settings(n, value):
        settings_dict = {
            1 : "DoNotResetColor",
            2 : "DefaultForegroundColor",
            3 : "DefaultBackgroundColor",
            4 : "DefaultStyle",
            5 : "LastForegroundColor",  # ---|
            6 : "LastBackgroundColor",  #    |--> USER CANNOT EDIT THEM! ~MEOW~
            7 : "LastStyle",            # ---|
            8 : "ForceDisableColoramaProxyObject"
        }

        if str(n).isnumeric():
            if 0 < n and n < 5 or n == 8:
                pass
            else:
                raise Exception("Not found that setting!")
        else:
            for i in range(1, 9):
                if settings_dict[i] != n:
                    vaildN = False
                else:
                    vaildN = True
                    n = i
                    break
            
            if vaildN == False:
                raise Exception("Not found that setting!")
        
        set_settings(n, value)

    def clear_settings():
        from os import remove
        try:
            remove('PrintWithColor.settings')
        except:
            pass
        del remove

    def all_colors():

        print("256 colors! Thanks ANSI support 8-bit colors", f='white', b='black')
        print("and right now, you can happy with me that")
    
        for a in range(0, 16):
            for b in range(0, 16):
                code = str(a * 16 + b)
                print(u"\u001b[38;5;" + code + "m " + code.rjust(3), end = ' ')
            print('')
        print('')

        c = -1
        for i in "Don't worry, some old terminal apps don't support all 256 colors, but 16 colors!\nBut you still using some alternatives too, to display full 256 colors!":
            c = c+1
            d = str(c)
            print("\u001b[38;5;" + d + "m" + i, end='', sep='')
            if c == 255:
                c = -1

        print("\u001b[0m")

print.clear_settings() # Clear all settings when startup, make sure to not to accidentally using old modules!