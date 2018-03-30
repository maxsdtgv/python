from tkinter import*

class But_print:
    # def __init__(self):


    def start(self):
        self.root = Tk()
        #self.root.pack()
        self.but = Button(self.root)
        self.but["text"] = "Hren"
        self.but.pack()
        self.root.mainloop()
