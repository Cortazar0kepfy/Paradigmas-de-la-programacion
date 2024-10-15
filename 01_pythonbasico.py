#Cortazar Tinajero Luis Enrique..
#paradigmas de la progranacion...
#=====================================
'''Este es un supercomentario
'''
#operaciones basicas
#=================
print(2+4)
print(2*3)
print(2**9)
print(2**0.5)     #raiz cuadrada
print(10%2)
print(10%0.1)    #exclusivo en python.

#===============================
#para saber el tipo de objeto
#====
y=0
print(type(y)) #entero
y=3.0
print(type(y))
y= True
print(type(y))     #boleano


#========================
#mensajes pantalla
#===============
print("Este es un comando de python. ","Este es otro enunciado.", y)
print('d',1)
print('nombres ', 'steve')
print('apellidos ', 'jobs')
print("vamos a sumar esto"+ "con esto otro")

#Continuar una instruccion en varios renglones............
if 100 > 99 and \
        200<=300 and \
        True != False:
            print('hola a todos')


#comandos diferentes en la misma linea..
print('hola'); print("tu")   #se considera mala practica

#usando parentesis redondos, cuadrados o llaves
#se puede escribir en varios renglones.

lista = [1 , 2 , 3 ,
        4 , 5 , 6 , 7 ,
        7 , 8 , 9 , 10 ,
        11, 12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]
print(lista)
print(matriz)

#identacion estricta para procesos dependientes de :(dos puntos)
if 10>5:
    print("diez es mayor que cinco") 
    print("otra identacion")
for i in lista:
    print(i)
    print("okkkkkkk")
if 10>5:
    print("verdadero")
    if 10<20:
        print("verdadero")
elif 5>3: #comienza segundo condicional
    print("esto no se imprimira")
else:
    print("aqui nunca llego")

#funciones

def saludar(nombre):
    print("hola", nombre)
    print("Bienvenido al tutorial de python")

saludar("Cortazar")




