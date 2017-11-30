import turtle

turtle.speed(5)
turtle.circle(50)
turtle.begin_fill()           #画头
turtle.circle(85)
turtle.fillcolor("blue")
turtle.end_fill()

# turtle.penup()
# turtle.goto(0,20)
# turtle.pendown()

# turtle.begin_fill()
# turtle.circle(35)
# turtle.fillcolor("white")
# turtle.end_fill()

turtle.begin_fill()                #画脸
turtle.circle(60)
turtle.fillcolor("white")
turtle.end_fill()



turtle.penup()
turtle.goto(-20,95)             #化左眼眶
turtle.pendown()
turtle.begin_fill()
turtle.circle(19)
turtle.fillcolor("white")
turtle.end_fill()



turtle.penup()                  #画右眼眶
turtle.goto(20,95)
turtle.pendown()
turtle.begin_fill()
turtle.circle(19)
turtle.fillcolor("white")
turtle.end_fill()

turtle.penup()                 #化左眼珠
turtle.goto(-8,111)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(3)
turtle.end_fill()


turtle.penup()              #画右眼珠
turtle.goto(8,111)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(3)
turtle.end_fill()

turtle.penup()              #画鼻子
turtle.goto(0,85)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.fillcolor("red")
turtle.end_fill()


turtle.goto(0,30)               #画竖线

turtle.penup()            #左边第一根胡子
turtle.goto(-20,70)
turtle.pendown()
turtle.goto(-45,80)

turtle.penup()                  #左边第二根胡子
turtle.goto(-20,60)
turtle.pendown()
turtle.goto(-47,60)

turtle.penup()                  #左边第三根胡子
turtle.goto(-20,50)
turtle.pendown()
turtle.goto(-47,40)

turtle.penup()                  #右边第三根胡子
turtle.goto(20,50)
turtle.pendown()
turtle.goto(47,40)


turtle.penup()                  #右边第二根胡子
turtle.goto(20,60)
turtle.pendown()
turtle.goto(47,60)


turtle.penup()                  #左边第一根胡子
turtle.goto(20,70)
turtle.pendown()
turtle.goto(45,80)

turtle.penup()                  #右边胳膊1
turtle.goto(50,20)
turtle.pendown()
turtle.goto(100,-10)


turtle.penup()                  #右边胳膊2
turtle.goto(50,-20)
turtle.pendown()
turtle.goto(80,-40)

turtle.begin_fill()
turtle.goto(100,-10)
turtle.goto(50,20)
turtle.goto(50,-20)
turtle.goto(80,-40)
turtle.fillcolor("yellow")
turtle.end_fill()



turtle.penup()                  #右手
turtle.goto(100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.fillcolor("blue")
turtle.end_fill()



turtle.penup()                  #左边胳膊1
turtle.goto(-50,20)
turtle.pendown()
turtle.goto(-100,-10)


turtle.penup()                  #左边胳膊2
turtle.goto(-50,-20)
turtle.pendown()
turtle.goto(-80,-40)

turtle.begin_fill()
turtle.goto(-100,-10)
turtle.goto(-50,20)
turtle.goto(-50,-20)
turtle.goto(-80,-40)
turtle.fillcolor("yellow")
turtle.end_fill()

turtle.penup()                  #左手
turtle.goto(-100,-53)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.fillcolor("blue")
turtle.end_fill()


turtle.penup()                  #左手
turtle.goto(-50,-20)
turtle.pendown()
turtle.goto(-50,-100)

turtle.penup()                  #左手
turtle.goto(50,-20)
turtle.pendown()
turtle.goto(50,-100)


turtle.begin_fill()
turtle.penup()
turtle.goto(50,-120)
turtle.pendown()
turtle.circle(10)
turtle.fillcolor("blue")
turtle.end_fill()

turtle.begin_fill()
turtle.goto(20,-120)
turtle.circle(10)
turtle.fillcolor("blue")
turtle.end_fill()


turtle.penup()
turtle.goto(50,-100)
turtle.pendown()
turtle.goto(20,-100)



turtle.penup()
turtle.goto(-50,-120)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.goto(-20,-120)
turtle.circle(10)
turtle.fillcolor("blue")
turtle.end_fill()

turtle.penup()
turtle.goto(-20,-100)
turtle.pendown()
turtle.goto(-50,-100)


turtle.penup()
turtle.goto(-20,-100)
turtle.pendown()
turtle.goto(-20,-85)

turtle.goto(20,-85)
turtle.goto(20,-100)

turtle.penup()
turtle.goto(-50,-20)
turtle.pendown()

turtle.begin_fill()
turtle.goto(50,-20)
turtle.goto(50,-85)
turtle.goto(-50,-85)
turtle.goto(-50,-20)
turtle.fillcolor("blue")
turtle.end_fill()


turtle.penup()
turtle.goto(0,-20)    #铃铛
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.fillcolor("yellow")
turtle.end_fill()



turtle.penup()
turtle.goto(-10,-10)
turtle.pendown()
turtle.goto(10,-10)


turtle.penup()
turtle.goto(-50,20)
turtle.pendown()
turtle.begin_fill()
turtle.goto(50,20)
turtle.goto(50,0)
turtle.goto(-50,0)
turtle.goto(-50,20)
turtle.fillcolor("red")
turtle.end_fill()


turtle.penup()
turtle.goto(50,0)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.fillcolor("red")
turtle.end_fill()


turtle.penup()
turtle.goto(-50,0)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.fillcolor("red")
turtle.end_fill()


turtle.penup()                  #内裤
turtle.goto(-50,-70)
turtle.pendown()
turtle.begin_fill()
turtle.goto(50,-70)
turtle.goto(50,-50)
turtle.goto(-50,-50)
turtle.goto(-50,-70)
turtle.fillcolor("red")
turtle.end_fill()

turtle.penup()
turtle.goto(-10,-70)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-10,-85)
turtle.goto(10,-85)
turtle.goto(10,-70)
turtle.goto(-10,-70)
turtle.fillcolor("red")
turtle.end_fill()

turtle.penup()
turtle.goto(-100,200)
turtle.pendown()
s = "机器猫中的战斗猫"
turtle.write(s,font = ("Arial",20,"normal"))


turtle.done()