#Cortázar Tinjero Luis Enrique 

#Gráficos usando la tortuga que pinta al caminar 
import turtle 
tortuga = turtle.Turtle()
tortuga.left(90)    #Giro a la izquierda con un ángulo de 90
tortuga.speed(500) #Velocidad de la tortuga


#Con ángulos de 90 es un árbol H
#  . Ósea:
angulo:float = 90


#El árbol se construye con recurisividad
# . .    .       .       .   .          . 


def arbol(i:float,angulo:float):
    if i<10.00:
        return
    else:
        tortuga.forward(i) #Camina i
        tortuga.left(angulo) #Gira a la izquierda 90 grados
        arbol(3.0*i/4.25,angulo)  #Pide otro árbol y cambia la longitud del paso
        tortuga.right(2*angulo)
        arbol(3.0*i/4.25,angulo)
        tortuga.left(angulo)
        tortuga.backward(i)

arbol(100,angulo)
turtle.done()

