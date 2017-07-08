# Python Ver:   3.6.1
#
# Author:       John S. Goya
#
# Purpose:      Phonebook demo MAIN
#

from tkinter import *
import tkinter as tk

#import other modules (separate files for gui & functions)
import phonebook_gui
import phonebook_function

# Frame is the Tkinter frame class
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #master frame config
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        #center_window - centers app on screen
        phonebook_function.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        #self.master is to catch if user clicks upper corner "x"
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_function.ask_quit(self))
        arg = self.master

        #load GUI widgets.
        phonebook_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
