#!/usr/bin/python

import turtle

turtle.speed(10)
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
turtle.write("Autosomes",font=("Arial",20))

def draw_chromosome():
    turtle.forward(60)
    turtle.left(30)
    turtle.forward(10)
    turtle.right(60)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(120)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(120)
    turtle.left(30)
    turtle.forward(10)
    turtle.right(60)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(60)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)
def turtle_turn():
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)
    turtle.left(30)
    turtle.forward(10)

turtle.penup()
turtle.goto(-200,180)
turtle.pendown()
#turtle.pencolor("green")
turtle.right(90)
draw_chromosome()

turtle.penup()
turtle.goto(-150,180)
turtle.pendown()
#turtle.pencolor("red")

turtle.left(30)
draw_chromosome()

turtle.penup()
turtle.goto(-80,0)
turtle.pendown()
turtle.write("Mutation\n creates \na sex-\ndetermining\n locus",font=("Arial",12))

turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.write("Proto\n X",font=("Arial",18))

turtle.penup()
turtle.goto(50,200)
turtle.pendown()
turtle.write("Proto\n Y",font=("Arial",18))


turtle.penup()
turtle.goto(0,180)
turtle.pendown()
#turtle.pencolor("green")

turtle.left(30)
draw_chromosome()

turtle.penup()
turtle.goto(50,180)
turtle.pendown()
#turtle.pencolor("red")

turtle.left(30)
turtle.forward(60)
turtle.left(30)
turtle.forward(10)
turtle.right(60)
turtle.forward(10)
turtle.left(30)
turtle.forward(60)
turtle.pencolor("red")
turtle.left(90)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
turtle.left(180)
turtle.forward(10)
turtle.pencolor("black")
turtle.forward(50)
turtle_turn()
turtle.left(30)
turtle.forward(50)
turtle.pencolor("red")
turtle.forward(10)
turtle.pencolor("black")
turtle.forward(60)
turtle.left(30)
turtle.forward(10)
turtle.right(60)
turtle.forward(10)
turtle.left(30)
turtle.forward(60)
turtle_turn()

turtle.penup()
turtle.goto(120,0)
turtle.pendown()
turtle.write("Mutation\n creates \na sexually-\nantagonistic\n locus\n(Male \nbeneficial)",font=("Arial",12))

turtle.penup()
turtle.goto(200,200)
turtle.pendown()
turtle.write("Proto\n X",font=("Arial",18))

turtle.penup()
turtle.goto(250,200)
turtle.pendown()
turtle.write("Proto\n Y",font=("Arial",18))

turtle.penup()
turtle.goto(200,180)
turtle.pendown()

turtle.left(30)
draw_chromosome()

turtle.penup()
turtle.goto(250,180)
turtle.pendown()

turtle.left(30)
turtle.forward(60)
turtle.left(30)
turtle.forward(10)
turtle.right(60)
turtle.forward(10)
turtle.left(30)
turtle.forward(40)
turtle.pencolor("yellow")
turtle.left(90)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
turtle.left(180)
turtle.forward(10)
turtle.pencolor("black")
turtle.forward(10)
turtle.pencolor("red")
turtle.left(90)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
turtle.left(180)
turtle.forward(10)
turtle.pencolor("black")
turtle.forward(50)
turtle_turn()
turtle.left(30)
turtle.forward(50)
turtle.pencolor("red")
turtle.forward(10)
turtle.pencolor("black")
turtle.forward(10)
turtle.pencolor("yellow")
turtle.forward(10)
turtle.pencolor("black")
turtle.forward(40)
turtle.left(30)
turtle.forward(10)
turtle.right(60)
turtle.forward(10)
turtle.left(30)
turtle.forward(60)
turtle_turn()

turtle.penup()
turtle.goto(-270,-200)
turtle.pendown()
turtle.write("Inversion\n happens",font=("Arial",12))

turtle.penup()
turtle.goto(-200,-100)
turtle.pendown()
turtle.write("Proto\n X",font=("Arial",18))

turtle.penup()
turtle.goto(-150,-100)
turtle.pendown()
turtle.write("Proto\n Y",font=("Arial",18))

turtle.penup()
turtle.goto(-200,-120)
turtle.pendown()
turtle.left(30)
draw_chromosome()

turtle.penup()
turtle.goto(-150,-120)
turtle.pendown()
turtle.left(30)
turtle.forward(20)
turtle.left(90)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
turtle.left(180)
turtle.forward(10)
turtle.pencolor("black")
turtle.forward(10)
turtle.left(90)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
turtle.left(180)
turtle.forward(10)
turtle.pencolor("black")
turtle.forward(10)
turtle.left(30)
turtle.forward(10)
turtle.right(60)
turtle.forward(10)
turtle.left(30)
turtle.forward(120)
turtle_turn()
turtle.left(30)
turtle.forward(120)
turtle.left(30)
turtle.forward(10)
turtle.right(60)
turtle.forward(10)
turtle.left(30)
turtle.forward(60)
turtle_turn()

turtle.penup()
turtle.goto(-100,-200)
turtle.pendown()
turtle.write("Mueller's Ratchet\n and DELETION\n of regions",font=("Arial",12))

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.write("Proto\n X",font=("Arial",18))

turtle.penup()
turtle.goto(50,-100)
turtle.pendown()
turtle.write("Proto\n Y",font=("Arial",18))

turtle.penup()
turtle.goto(0,-120)
turtle.pendown()
turtle.left(30)
draw_chromosome()

turtle.penup()
turtle.goto(50,-140)
turtle.pendown()
turtle.left(30)
turtle.forward(15)
turtle.left(90)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
turtle.left(180)
turtle.forward(10)
turtle.pencolor("black")
turtle.forward(5)
turtle.left(90)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(36)
turtle.right(90)
turtle.forward(10)
turtle.end_fill()
turtle.left(180)
turtle.forward(10)
turtle.pencolor("black")
turtle.forward(10)
turtle.left(30)
turtle.forward(10)
turtle.right(60)
turtle.forward(10)
turtle.left(30)
turtle.forward(60)
turtle_turn()
turtle.left(30)
turtle.forward(60)
turtle.left(30)
turtle.forward(10)
turtle.right(60)
turtle.forward(10)
turtle.left(30)
turtle.forward(50)
turtle_turn()

turtle.done()
