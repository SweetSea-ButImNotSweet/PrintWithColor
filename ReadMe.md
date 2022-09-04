# **PrintWithColor**

A tiny Python wrapper that enhances the print() syntax by enabling text coloring on the screen.


> **WARNING!** Vietnamese version of ReadMe.md is outdated. Sorry, but I don't have time to edit it.<br>Please use English version for reference

> **NOTE:** All the comment in the source code still not translated completely, it may have some errors.<br>You don't understand something? Just ask me in [Issues](https://github.com/SweetSea-ButNotSweet/PrintWithColor/issues), and I will try to read and answer all :smile:<br>Thanks

# **Installion**
To install this package via PyPi, type like this command below to the Terminal or Command Prompt:

```bat
pip install PrintWithColor
```
> For those of you who are wondering why I don't put the \$ character in front of the command as others do in other projects, here's why.

> Because ***forgetting*** to __DELETE__ ***the extra \$ character*** while pasting the command will result in the command __*FAILING!*__.
> This command may also be used on Windows, however on Linux, you should replace pip with pip3 (if you use pip, maybe Linux will call Python 2 instead Python 3!)

# **Usage**
This is the basic usage of **PrintWithColor**
> **WARNING! DO NOT IMPORT PRINTWITHCOLOR.PRINTWITHCOLORCORE!** (ALTHOUGH YOUR IDE SHOW IT!)


```python
from PrintWithColor import print as print
print('Hello, I am a green line!', f = 'green', b= 'black')
print('Or a line with a cyan background', f = 'black', b = 'cyan')
```

### All argument in print() **from Python**

| Argument      | Description                                                                                                                                                                                                                                                                                                                          | DefaultValue |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| textfrominput | The content you want to display on the screen, allows you to enter many arguments                                                                                                                                                                                                                                                    | Any          |
| sep           | A separate sign between the items in textfrominput argument (if there is only one argument in textfrominput, it will not appear anywhere)                                                                                                                                                                                            | ' '          |
| end           | Ending character, when there is only one argument or when textfrominput has reached its final argument, the ending character appears.                                                                                                                                                                                                | '\n'         |
| file          | Where should the text be output? The default in Python is sys.stderr or your screen.<br><br> If the file argument is a __writable file__, Python will automatically __write to the file__ provided in the file argument instead of writing to the screen.<br><BR>If that file cannot be written, __an exception will be raised__ [1] | None         |
| flush         | Should the buffer be cleaned up once the results are printed?                                                                                                                                                                                                                                                                        | False        |

### All argument in Print() syntax **from PrintWithColor**

| Argument      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Default |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| textfrominput | The content you want to display on the screen, allows you to enter many arguments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Any     |
| sep           | A separate sign between the arguments (if there is only one argument in textfrominput, it will not appear anywhere)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | ' '     |
| end           | Ending character, when there is only one argument or when textfrominput has reached its final argument, the ending character appears.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | '\n'    |
| file          | Where should the text appear?<br>This wrapper will use the Colorama library's proxy object by default.<br><br>If the file argument is a __writeable file__, PrintWithColor will write the output to that file, ***just like the original print() syntax***.<br><br>PrintWithColor will __skip the file__ provided in it and __display the text on the screen__ only if it is not writeable (or read-only) and ForceDisableColoramaProxyObject still False.<br><br>~~You should also be aware that in order to use Colorama's proxy object, this argument will __skip__ ***all objects other than a writeable file!*** (Because this wrapper is cross-platform, I should use Colorma's proxy object to avoid any bugs/issues that may happen!)~~<br><br> From 0.0.2, PrintWithColor will not try to force you to using Colorama's proxy object (if you use it when you combine 4-bit and 8-bit colors, 8-bit colors will be white as default). That why you will have a option to force PrintWithColor not to use Colorama's proxy object | None    |
| flush         | Should the buffer be cleaned up once the results are printed?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | False   |
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |         |
| f             | Foreground color [2] [3]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | WHITE   |
| b             | Background color [2] [3]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | BLACK   |
| s             | Style(s)/Decoration(s) of the text [2] [4]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | NORMAL  |



> **NOTE FOR PRINT() SYNTAX BETWEEN PYTHON AND PRINTWITHCOLOR**

1. If the file argument is a read-only file. It will throw an exception in Python, but PrintWithColor will automatically ignore that argument and print the output directly to the screen.
> **Start from 0.0.2**, PrintWithColor will change BRIGHT, DIM, NORMAL
2. You can write the colour in uppercase or lowercase as well
3. Acceptable color ranges are WHITE, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BLACK
4. Acceptable color styles are BOLD, ITALIC, REVERSED

> **STARTING FROM 0.0.2**, PrintWithColor will recieve the color with style in argument f (foreground color)<br>**EXAMPLE**:
> ```python
> print("Bright blue", f = "B BLUE")
> print("Dim    cyan", f = "D CYAN")
> ```
> With B is bright and D is dim

> **WARNING!** Windows will **NOT** correctly display dark (dim) colors. So, in most cases, you won't notice a change if you put a when you leave text with dark color between text with normal one.<br><br>(**Don't blame me or the author of Colorama**, this is because __Windows doesn't support__ ***ANSI 'dim text'*** :cry:)<br><br> **For more infomation:** Please look down to the last line of colorama's description: https://github.com/tartley/colorama#description


# **Additional configuration**

> **WARNING!**: If any of these settings are invalid, they will be reset to their **DEFAULT** values!<br>
> **How to change configuration?** using print.change_settings() syntax

## **1. DoNotResetColor**


> **Effect:** Not reset color after every print() syntax is performed<br>
> **Default value:** False **(boolean)**<br>
> **Acceptable value:** True, False **(boolean)**


```python
print.change_settings(1, True)
# or
print.change_settings('DoNotResetColor', True)
# will return the same results!

# When using
print('Line 1', f='black', b='green')
print('Line 2 must be formatted in the same color as line 1!')
```

## **2. DefaultForegroundColor**

> **Effect:** Change the default foreground color (When you're done with the print() syntax and the variable **DoNotResetColor = False**, the following print() syntax will use the color you specified!)<br>
> **Default value:** WHITE **(string)**<br>
> **Acceptable value:** WHITE, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BLACK


```python
print.change_settings(2, 'GREEN')
# or
print.change_settings('DefaultForegroundColor', 'GREEN')
# will return the same results!

# When using
print('Even without the f argument, this line must be green!')
```

## **3. DefaultBackgroundColor**

> **Effect:** Change the default background color (When you're done with the print() syntax and the variable **DoNotResetColor = False**, the following print() syntax will use the color you specified!)<br>
> **Default value:** BLACK **(string)**<br>
> **Acceptable value:** WHITE, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BLACK


```python
print.change_settings(3, 'GREEN')
# or
print.change_settings('DefaultBackgroundColor', 'GREEN')
# will return the same results!

# When using
print('This line will have nice green background, although I don\'t use b argument')
```

## **4. DefaultStyle**

> **Effect:** Change the default style of foreground color (When you're done with the print() syntax and the variable **DoNotResetColor = False**, the following print() syntax will use the style you specified!)<br>
> **Default value:** NORMAL **(string)**<br>
> **Acceptable value:** DIM, NORMAL, BRIGHT


```python
print.change_settings(4, 'NORMAL')
# or
print.change_settings('DefaultStyle', 'NORMAL')

# Example
print.change_settings('DefaultStyle', 'NORMAL')
print.change_settings('DoNotResetColor', 'True')

print('Line 1 will have a normal-green color', f='green')
print('But this line will have a bright color'), s='bright') 
```

## **5. clear_settings()** (Reset all settings of PrintWithColor)

> **Effect:** Clear all PrintWithColor's settings!<br>
> **NO ARGUMENT & NO WARNING & NO OUTPUT!**
> 
```python
print.clear_settings()
```
## **8. ForceDisableColoramaProxyObject** (Try to avoid using Colorama's Proxy Object)

> **NOTE:** You may don't need this settings, in most cases<br>Why? Because PrintWithColor will avoid using Colorama's Proxy Object if you are using 4-bit colors with 8-bit colors, or using file argument<br>
> **NO ARGUMENT & NO WARNING & NO OUTPUT!**
```python
print.change_settings(8, True)
# or
print.change_settings('ForceDisableColoramaProxyObject', True)
```

# Problem? Question?
Questions, problem: don't hestitate ask me on [Issues](https://github.com/SweetSea-ButNotSweet/PrintWithColor/issues)<br>
Contact me? [Right here](https://github.com/SweetSea-ButNotSweet/SweetSea-ButNotSweet/issues)