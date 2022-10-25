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

def text_thing(text):
    print("Text:", text)
    # os.startfile(text)
    subprocess.run(["C:/Program Files/Inkscape/bin/inkscape.exe", text])

async def main():
    w = WindowManager((300, 150), text_thing)
    asyncio.create_task(w.create())

def create_window():
    logging.info("Creating Window")
    # print("AAA")
    w = WindowManager((300, 150), text_thing)
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


