import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.left(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,220)
myWin.exitonclick()