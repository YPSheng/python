from tkinter import *

class MovingBall:
    def __init__(self):
        win = Tk()
        win.title("Moving Ball")

        self.width = 250
        self.canvas = Canvas(win,width = self.width,height = 200,bg = 'white')
        self.canvas.pack()

        frame = Frame(win)
        frame.pack()
        btLeft = Button(frame,text = "Left",command = self.LeftMoving )
        btLeft.pack()
        btRight = Button(frame,text = "Right",command = self.RightMoving)
        btRight.pack()
        btUp = Button(frame,text = "Up",command = self.UpMoving)
        btUp.pack()
        btDown = Button(frame,text = "Down",command = self.DownMoving)
        btDown.pack()
        self.x = 0
        self.y = 0
        self.canvas.create_oval(self.x,self.y,self.x + 10,self.y + 10,fill = "black",tags = "oval")
        win.mainloop()

    def LeftMoving(self):
        self.canvas.delete("oval")
        if self.x > 10:
            self.x -= 10
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="black", tags="oval")
        else:
            self.x = 250
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="black", tags="oval")

    def RightMoving(self):
        self.canvas.delete("oval")
        if self.x < 250:
            self.x += 10
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="black", tags="oval")
        else:
            self.x = 0
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="black", tags="oval")
    def UpMoving(self):
        self.canvas.delete("oval")
        if self.y > 10:
            self.y -= 10
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="black", tags="oval")
        else:
            self.y = 200
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="black", tags="oval")

    def DownMoving(self):
        self.canvas.delete("oval")
        if self.y < 200:
            self.y += 10
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="black", tags="oval")
        else:
            self.y = 0
            self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill="black", tags="oval")
MovingBall()