# Call builtins library, allow me to use the pure print command in Python
import builtins
from PrintWithColor.PrintWithColorCore import *
# from PrintWithColorCore import *

# Sorry everyone, all this code still not translated into English :[

# Lệnh Printc là 
class print():
#   Lưu ý: sep, end, flush được thêm vào nhằm giữ tương thích ngược với lệnh print

#                                                                                                                   s là kiểu màu chữ <--|
#                                                                                                                                        |
#                                                                                                 b là màu nền <--|                      |
#                                                                                                                 |                      |
#                                                                          f là màu chữ <--|                      |                      |
#                                                                                          |                      |                      |
    def __init__ (self, *textfrominput, sep = ' ', end = '\n', file = None, flush = False, f = 'ForegroundColor', b = 'BackgroundColor', s = 'Style',):
#                                        |          |                         |--> flush: dọn bộ đệm (mặc định là False)
#                                        |          |
#                                        |          |==> end là kí tự kết thúc hoàn toàn lệnh print
#                                        |
#                                        |--> sep hay seperate tách từng item nếu textfrominput có hơn 2 đối tượng
        
        # Riêng đối số file không có tác dụng gì, bởi mặc định file bị giữ chân bởi Colorama
        # Vì wrapper này viết cho Windows là chính, nên mình cũng không quan tâm lắm với Linux
        # nhưng nếu có thời gian sẽ test thử trên Linux sau (còn MacOS thì nằm mơ, nhà mình không có máy Mac đâu mà đòi kêu ca sửa lỗi)

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

        printToComputer(self, *textfrominput, sep = ' ', end = '\n', file = None, flush = False, f = get_settings(5), b = get_settings(6), s = get_settings(7),)

# get_settings() sẽ trả kết quả như sau
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
        }

        if str(n).isnumeric():
            if 0 < n and n < 5:
                pass
            else:
                raise Exception("Not found that setting!")
        else:
            for i in range(1, 5):
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

print.clear_settings() # Clear all settings when startup, make sure to not to accidentally using old modules!