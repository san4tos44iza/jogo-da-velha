from turtle import Turtle,onscreenclick, onkey, listen, Screen
turtle = Turtle ()
tela = Screen()
turtle.speed(0)
resultado = 0
numero = 0

def trocar ():
global resultado
global numero
numero = numero + 1
resultado = numero % 2


turtle.forward(100)
turtle.backward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(180)
turtle.forward(100)
turtle.forward(100)
turtle.backward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(180)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.backward(100)
turtle.right(90)
turtle.forward(100)
turtle.backward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.backward(300)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.backward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)


def jogar(x, y):
turtle.penup()
turtle.goto(x, y)
if resultado == 0:
x2()
if resultado == 1:
circulo()
trocar()

def circulo():
turtle.color('blue')
r = 50
turtle.pendown()
turtle.circle(r)

def x2():
turtle.color('pink')
turtle.pendown()
turtle.right(45)
