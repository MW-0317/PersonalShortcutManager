from tkinter import *
import os
import typing
import logging

class TextWindow(Tk):
    def __init__(self, size: tuple, callback, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.initialize(size)
        self.callback = callback
        self.curr_files = []

    def initialize(self, size: tuple):
        self.configure(background="#2a3833")
        self.geometry('{}x{}'.format(size[0], size[1]))
        self.center()
        self.lock(size)
        self.overrideredirect(True)
        # self.wm_attributes('-fullscreen', 'True')
        self.attributes('-topmost', True)

        self.sv = StringVar()
        self.sv.trace_add("write", self.file_selector)


        self.e = Entry(self, textvariable=self.sv, width=100, relief=FLAT, bg="#2a3833", fg="white", font=('Cambria 24'), validate="focusout", validatecommand=self.destroy)
        # self.e = Entry(self, textvariable=self.sv, width=100, font=('Cambria 24'))
        self.e.pack(padx=0, pady=0)
        self.focus_force()
        self.e.focus_set()

        self.bind('<Return>', self.submit)

        self.labels = []
        self.file_selector(None, None, None)
        


    def center(self):
        self.eval('tk::PlaceWindow . center')
    
    def lock(self, size=(300, 150)):
        self.bind_all("<Configure>", lambda x: self.geometry('{}x{}'.format(size[0], size[1])))

    def submit(self, event):
        value = self.e.get()
        self.destroy()
        # print(value)
        if self.curr_files:
            self.callback(self.curr_files[0])
        else:
            self.callback("")
        # self.callback(value)
    
    def file_selector(self, var, index, mode):
        print(self.sv.get())
        filtered_files = [i for i in os.listdir(os.curdir) if i.endswith(".svg") and i.startswith(self.sv.get())] # 
        self.curr_files = filtered_files
        self.destroy_all_labels()
        self.create_labels(filtered_files)
        self.pack_all_labels()

    def latex(self, var, index, mode):
        pass

    def create_labels(self, list):
        i = True
        for item in list:
            if i:
                self.labels.append(Label(self, width=self.winfo_screenwidth(), background='#2cde65', text=item, font=('Cambria 18')))
            else:
                self.labels.append(Label(self, width=self.winfo_screenwidth(), background='#2a3833', text=item, font=('Cambria 18')))
            i = False

    def pack_all_labels(self):
        for label in self.labels:
            label.pack()

    def destroy_all_labels(self):
        for label in self.labels:
            label.destroy()
        self.labels = []


class WindowManager:
    def __init__(self, size: tuple, callback):
        self.size = size
        self.callback = callback
        
    def create(self):
        logging.info("Creating TextWindow")
        TextWindow(self.size, self.callback)
        mainloop()


if __name__ == "__main__":
    # master = TextWindow((300, 150))
    master = TextWindow((500, 40), lambda x: 0)
    mainloop()