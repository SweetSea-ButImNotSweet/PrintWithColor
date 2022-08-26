import subprocess
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

subprocess.run(['jupyter.exe', 'nbconvert', '--to', 'markdown', file_path])