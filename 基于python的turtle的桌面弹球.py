from tkinter import *
from random import randint

def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0,15))
    return color
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:
        return chr(hexValue - 10 + ord("A"))
class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 2
        self.dy = 2
        self.radius = 3
        self.color = getRandomColor()

class BounceBalls:
    def __init__(self):
        self.ballList = []
        win = Tk()
        win.title("Bouncing Balls")

        self.width = 350
        self.height = 150
        self.canvas = Canvas(win,bg = "white",width = self.width,height = self.height)
        self.canvas.pack()


        frame = Frame(win)
        frame.pack()
        btStop = Button(frame,text = "Stop",command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame,text = "Resume",command = self.resume)
        btResume.pack(side = LEFT)
        btAdd = Button(frame,text = "+",command = self.add)
        btAdd.pack(side = LEFT)
        btRemove = Button(frame,text = "-",command = self.remove)
        btRemove.pack(side = LEFT)


        self.sleepTime = 100
        self.isStopped = False
        self.animate()
        win.mainloop()
    def stop(self):
        self.isStopped = True
    def resume(self):
        self.isStopped = False
        self.animate()
    def add(self):
        self.ballList.append(Ball())
    def remove(self):
        self.ballList.pop()
    def animate(self):
        while not self.isStopped:
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            self.canvas.delete("ball")

            for ball in self.ballList:
                self.redisplayBall(ball)
    def redisplayBall(self,ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx
        if ball.y > self.height or ball.y < 0:
            ball.y = -ball.y
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius,ball.y - ball.radius,ball.x + ball.radius,ball.y + ball.radius,fill = ball.color,tags = "ball")
BounceBalls()