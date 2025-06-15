#Cortázar Tinajero Luis Enrique.
import numpy as np
import turtle

def calcular_determinante(matriz):
    return np.linalg.det(matriz)


matriz = np.array([[3, 2], [1, 4]])
determinante = calcular_determinante(matriz)
print(f"Determinante: {determinante}")
#Opcional:Visualización con turtle.
t = turtle.Turtle()
t.penup()
t.goto(-50, 50)
t.pendown()

for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()


