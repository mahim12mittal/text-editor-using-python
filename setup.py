import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Mahim\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mahim\AppData\Local\Programs\Python\Python38\tcl\tcl8"

executables = [cx_Freeze.Executable("mpad.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Mah text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico","tcl86t.dll","tk86t.dll", "icons"]}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
