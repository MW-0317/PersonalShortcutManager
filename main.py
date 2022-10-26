import asyncio

from sympy import loggamma
from textwindow import WindowManager
import os
import subprocess
from listener import Listener
import threading
import logging
import sys

global total_windows
total_windows = []

def inkscape_open(text):
    print("Text:", text)
    # os.startfile(text)
    subprocess.run(["inkscape.exe", text])

def create_window():
    logging.info("Creating Window")
    # print("AAA")
    w = WindowManager((300, 150), inkscape_open)
    # w.create()
    # total_windows.append(w)
    # print(total_windows)
    t = threading.Thread(target=w.create)
    t.start()

    
def m():
    Listener.basic_hotkeys({'<shift>+<ctrl>+a':create_window})

# asyncio.run(main())
os.chdir(sys.argv[1])
m()


