# -*- coding: utf-8 -*-
# Created by Marc-Alexandre Blanchard

from tkinter import *
class Application(object):
    """ classe application """
    
    def triplet(self,rgb):
        return format((rgb[0]<<16)|(rgb[1]<<8)|rgb[2], '06x')

    def updateUI(self):
        color = "#"+self.triplet((self.varR.get(),self.varG.get(),self.varB.get()))
        self.cadre.create_rectangle(0, 0, 200, 200,  fill=color)
        color=color.upper()
        self.textH.config(text=color)
        
    def __init__(self):
        self._tk = Tk()
        self._tk.title("ColourTool")
        self._tk.resizable(width=False, height=False)

        self.conteneur1= Frame(self._tk)

        self.cadre = Canvas(self._tk, width=200, height=200)
        color = "#"+self.triplet((255, 255, 255))
        color=color.upper()
        self.cadre.create_rectangle(0, 0, 200, 200,  fill=color)
        self.cadre.grid(row=0, column=2,rowspan=7)

        self.textH= Label(self._tk, text = color)
        self.textH.grid(row=4, column=1,columnspan=1)

        self.textR= Label(self._tk, text = "Red")
        self.textR.grid(row=0, column=0)
        self.textG= Label(self._tk, text = "Green")
        self.textG.grid(row=1, column=0)
        self.textB= Label(self._tk, text = "Blue")
        self.textB.grid(row=2, column=0)

        self.varR = IntVar()
        self.varG = IntVar()
        self.varB = IntVar()
        
        self.red = Scale(self._tk,length=300,resolution=1,tickinterval=128, from_=0, to=255,orient=HORIZONTAL,variable=self.varR,command = lambda x=self.varR : self.updateUI())
        self.red.grid(row=0, column=1)
        self.green = Scale(self._tk,length=300,resolution=1,tickinterval=128, from_=0, to=255,orient=HORIZONTAL,variable=self.varG,command = lambda x=self.varG : self.updateUI())
        self.green.grid(row=1, column=1)
        self.blue = Scale(self._tk,length=300,resolution=1,tickinterval=128, from_=0, to=255,orient=HORIZONTAL,variable=self.varB,command = lambda x=self.varB : self.updateUI())
        self.blue.grid(row=2, column=1)

    def mainloop(self):
        self._tk.mainloop()

if __name__ == '__main__':
    Application().mainloop()
