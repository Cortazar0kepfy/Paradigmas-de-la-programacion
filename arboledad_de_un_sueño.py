#Cortázar Tinajero Luis Enrique.....


import turtle
tortuga = turtle.Turtle()
tortuga.color("Red")
tortuga.pensize(3)

import random
def arbol(i:float, angulo:float):
    if i < 10.00:
        return
    else:
        tortuga.color(random.choice(["green", "brown", "dark green", "light green"]))
        tortuga.forward(i)
        tortuga.left(angulo)
        arbol(3.0 * i / 4.25, angulo)
        tortuga.right(2 * angulo)
        arbol(3.0 * i / 4.25, angulo)
        tortuga.left(angulo)
        tortuga.backward(i)




turtle.bgcolor("lightblue") #fondo azul cielo.
#función para dibujar hojas.

def hoja(x,y):
    tortuga.penup()
    tortuga.goto(x , y)
    tortuga.pendown()
    tortuga.color("darkgreen")
    tortuga.begin_fill()
    tortuga.circle(3) #Tamaño dd la hoja....


    import turtle
    tortuga = turtle.Turtle()
    tortuga.color("Red")
    tortuga.pensize(3)

    import random
    def arbol(i:float, angulo:float):
        if i < 10.00:
            return
        else:
            tortuga.color(random.choice(["green", "brown", "dark green", "light green"]))

                                         
        rtuga.forward(i)
tortugangulo)
arbol(3.0 * i / 4.25, angulo)
tortuga.right(2 * angulo)
arbol(3.0 * i / 4.25, angulo)
tortuga.left(angulo)
tortuga.backward(i)


turtle.bgcolor("lightblue") #fondo azul cielo.
#función para dibujar hojas.

def hoja(x,y):
    tortuga.penup()
    tortuga.goto(x , y)
    tortuga.pendown()
    tortuga.color("darkgreen")
    tortuga.begin_fill()
    tortuga.circle(3) 


    import turtle
    tortuga = turtle.Turtle()
    tortuga.color("Red")
    tortuga.pensize(3)

    import random
    def arbol(i:float, angulo:float):
        if i < 10.00:
            return
        else:
            tortuga.color(random.choice(["green", "brown", "dark green", "light green"
]))
tortuga.forward(i)
tortuga.left(angulo)
arbol(3.0 * i / 4.25, angulo)
tortuga.right(2 * angulo)
arbol(3.0 * i / 4.25, angulo)
tortuga.left(angulo)
tortuga.backward(i)


turtle.bgcolor("lightblue") #fondo azul cielo.
#función para dibujar hojas.

def hoja(x,y):
    tortuga.penup()
    tortuga.goto(x , y)
    tortuga.pendown()
    tortuga.color("darkgreen")
    tortuga.begin_fill()
    tortuga.circle(3) #Tamaño dd la hoja
