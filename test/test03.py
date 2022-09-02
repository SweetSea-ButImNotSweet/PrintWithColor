# NOTE: THIS TEST IS NOT RELATED TO PRINTWITHCOLOR! BUT IT WILL BE RUN IN PRINTWITHCOLOR TO DETECT IF YOUR TERMINAL IS SUPPORT
# 256 COLORS OR NOT
# THIS CODE IS BASED ON: https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

for a in range(0, 16):
    for b in range(0, 16):
        code = str(a * 16 + b)
        print(u"\u001b[38;5;" + code + "m " + code.rjust(3), end = ' ')
    print('')
print('')

c = -1
for i in "Do you see all 256 colors? If YES, congratulations!\nIf not, don't worry, some old terminal apps don't support all 256 colors, but 16 colors!":
    c = c+1
    d = str(c)
    print("\u001b[38;5;" + d + "m" + i, end='', sep='')
    if c == 255:
        c = -1

print("\u001b[0m")