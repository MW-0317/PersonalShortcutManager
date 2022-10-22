"""
Python Keyboard Listener
"""
from itertools import combinations
from logging.config import listen
from math import comb
from pynput import keyboard
import asyncio
import threading
import logging

class Listener:
    combs=set([])
    prev_combs=set([])
    def __init__(self):
       self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release) 

    def on_press(self, key):
        if key == keyboard.Key.esc:
            return False
        try:
            k = key.char
        except:
            k = key.name
        self.combs.add(k)
        if not self.combs == self.prev_combs:
            logging.info(self.combs)
            print(self.combs)
        self.prev_combs = self.combs.copy()

    def on_release(self, key):
        try:
            k = key.char
        except:
            k = key.name
        self.combs.remove(k)

    async def begin(self):
        asyncio.create_task(self.listener.run())
        # self.listener.start()
        # self.listener.join()
    
    def test_function():
        print('a')

    def basic_hotkeys(callback):
        hs = keyboard.GlobalHotKeys({
            '<ctrl>+<shift>+a' : callback
        })
        hs.start()
        hs.join()


if __name__ == "__main__":
    l = Listener()
    # t1 = threading.Thread(target=l.begin)

    asyncio.run(l.begin())