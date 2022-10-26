"""
Python Keyboard Listener
"""
from itertools import combinations
from logging.config import listen
from math import comb
from matplotlib.pyplot import hot
from pynput import keyboard
import asyncio
import threading
import logging

class Listener:
    
    def __init__(self, hotkeys={}):
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.combs=set([])
        self.prev_combs=set([])
        self.hotkeys = [

        ]
        for k, v in hotkeys.items():
            self.hotkeys.append((set(k.split("+")), v))
        # self.hotkeys = {
        # # hotkey: callback      # hotkey = key+key+key+...

        # }
        # for k, v in hotkeys:
        #     self.hotkeys["+".join(sorted(k.split("+")))] = v

    def on_press(self, key):
        if key == keyboard.Key.esc:
            return False
        try:
            k = key.char
        except:
            k = key.name
        print(key)
        self.combs.add(k)
        if not self.combs == self.prev_combs:
            for h in self.hotkeys:
                k = h[0]
                v = h[1]
                print(k, self.combs)
                if self.combs == k:
                    v()
        self.prev_combs = self.combs.copy()

    def on_release(self, key):
        try:
            k = key.char
        except:
            k = key.name
        self.combs.remove(k)
    
    def begin(self):
        self.listener.start()
        self.listener.join()

    def begin(self):
        # asyncio.create_task(self.listener.run())
        self.listener.start()
        self.listener.join()
    
    def test_function():
        print('a')

    def close():
        print("Closing")
        Listener.hs.stop()

    def basic_hotkeys(hotkeys):
        hotkeys['<shift>+<alt>'] = Listener.close
        Listener.hs = keyboard.GlobalHotKeys(hotkeys)
        Listener.hs.start()
        Listener.hs.join()


if __name__ == "__main__":
    def test():
        print("YIPPIE!")

    # l = Listener(hotkeys={
    #     'ctrl+shift+a' : test
    # })
    # t1 = threading.Thread(target=l.begin)
    # l.begin()
    # asyncio.run(l.begin())

    Listener.basic_hotkeys({})
