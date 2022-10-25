"""
Python Keyboard Listener
"""
from itertools import combinations
from logging.config import listen
from math import comb
from pynput import keyboard
import threading

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
            print(self.combs)
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

l = Listener()

threading.Thread(target=l.begin())
