from tkinter import *

class ToggleButton(Canvas):
    def __init__(self, root, command=None, fg='black', bg='gray', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(width=100, height=50, borderwidth=0, highlightthickness=0)
        self.root = root
        
        self.back_ground = self.create_arc((0, 0, 0, 0), start=90, extent=180, fill=bg, outline='')
        self.back_ground1 = self.create_arc((0, 0, 0, 0), start=-90, extent=180, fill=bg, outline='')
        self.rect = self.create_rectangle(0, 0, 0, 0, fill=bg, outline='')
        
        self.btn = self.create_oval(0, 0, 0, 0, fill=fg, outline='')

        self.bind('<Configure>', self._resize)
        self.bind('<Button>', self._animate, add='+')  
        self.bind('<Button>', command, add='+')

        self.state = 0

    def _resize(self, event):
        

        self.coords(self.back_ground, 5, 5, event.height-5, event.height-5)
        self.coords(self.back_ground1, 5, 5, event.height, event.height-5)
       
        factor = event.width-(self.coords(self.back_ground1)[2]-self.coords(self.back_ground1)[0])-10
        self.move(self.back_ground1, factor, 0)

        self.coords(self.rect, self.bbox(self.back_ground)[2]-2, 5, self.bbox(self.back_ground1)[0]+2, event.height-5)

        
        self.coords(self.btn, 5, 5, event.height-5, event.height-5)

        if self.state:
            self.moveto(self.btn, self.coords(self.back_ground1)[0]+4, 4)
                
    
    def _animate(self, event):
        x, y, w, h = self.coords(self.btn)
        x = int(x-1)
        y = int(y-1)
        
        
        if x == self.coords(self.back_ground1)[0]+4:
            self.moveto(self.btn, 4, 4)
            self.state = 0
            
        else:
            self.moveto(self.btn, self.coords(self.back_ground1)[0]+4, 4)
            self.state = 1
    
    def get_state(self):
        return self.state

#Your own function
def hello(event='Nooo'):
    print(event)
    if bool(btn.get_state()):
        print('State is 1')

    elif not bool(btn.get_state()):
        print('State is 0')
    
root = Tk()


btn = ToggleButton(root, lambda _:hello('Hello'), 'red', 'green')
btn.pack()

btn2 = ToggleButton(root, command=hello)
btn2.pack(expand=True, fill='both')

Button(root, text='Text').pack(expand=True, fill='both')

root.mainloop() 