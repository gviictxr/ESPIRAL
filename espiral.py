import turtle
import random

turtle.speed(0)  
turtle.bgcolor("black")  
turtle.pensize(4)  

def cor_aleatoria():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

for i in range(100):
    turtle.color(cor_aleatoria())  
    turtle.forward(5 * i)  
    turtle.left(90)  

turtle.done()
