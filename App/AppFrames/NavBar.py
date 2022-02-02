from re import S
import tkinter as tk
from cefpython3 import cefpython as cef
import os

class NavigationBar(tk.Frame):
    def __init__(self, parent):
        
        self.browser = None

        tk.Frame.__init__(self, parent)

        path=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/icons8-back-50.png"
        self.back_image = tk.PhotoImage(file=path).subsample(2,2)
        self.back_button = tk.Button(self, image=self.back_image, command=self.go_backward)
        self.back_button.grid(row=0, column=0)

        path=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/icons8-forward-50.png"
        self.fwd_image = tk.PhotoImage(file=path).subsample(2,2)
        self.fwd_button = tk.Button(self, image=self.fwd_image, command=self.go_forward)
        self.fwd_button.grid(row=0, column=1)
        
        path=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/icons8-rotate-50.png"
        self.reload_image = tk.PhotoImage(file=path).subsample(2,2)
        self.reload_button = tk.Button(self, image=self.reload_image, command=self.reload)
        self.reload_button.grid(row=0, column=2)


        self.url = tk.Entry(self)

        self.url.grid(row=0, column=3, columnspan=4,sticky=(tk.E+tk.W))     
        self.url.bind("<Return>", self.load_url)
        tk.Grid.rowconfigure(self, 0, weight=100)
        tk.Grid.columnconfigure(self, 3, weight=100)

        self.pack()
        
    def set_browser(self, browser):
        self.browser = browser
        


    def go_backward(self):
        if self.browser:
            self.browser.GoBack()

    def go_forward(self):
        if self.browser:
            self.browser.GoForward()

    def reload(self):
        if self.browser:
            self.browser.Reload()

    def set_url(self, url):
        self.url.delete(0, tk.END)
        self.url.insert(0, url)

    def load_url(self, event):
        if self.browser:
            self.browser.StopLoad()
            self.browser.LoadUrl(self.url.get())