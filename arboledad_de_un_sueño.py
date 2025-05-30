#Cortázar Tinajero Luis Enrique.....






import turtle
import random

# Configuración del entorno gráfico
turtle.bgcolor("lightblue")  # Fondo azul cielo
tortuga = turtle.Turtle()
tortuga.color("Red")
tortuga.pensize(3)
tortuga.speed(0)  # Aumenta la velocidad de dibujo
tortuga.left(90)  # Posiciona la tortuga para empezar el árbol hacia arriba

# Función para dibujar el árbol
def arbol(i: float, angulo: float):
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

# Función para dibujar hojas
def hoja(x, y):
    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()
    tortuga.color("darkgreen")
    tortuga.begin_fill()
    tortuga.circle(3)  # Tamaño de la hoja
    tortuga.end_fill()

# Dibuja el árbol principal
arbol(100, 30)

# Genera algunas hojas en posiciones aleatorias dentro del área del árbol
for _ in range(15):
    hoja(random.randint(-40, 40), random.randint(50, 120))

turtle.done()

