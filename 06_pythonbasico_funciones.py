#===================================================================================
# Cortazar Tinajero Luis Enrique.

# Mi primera funcion
def saludo():
    """Esta funcion saluda"""
    print('priviet, como estas?')

# Llamado de funcion
saludo()

# Funcion con argumento
def salu2(nombre):
    """Esta funcion te saluda por tu nombre"""
    print("QUE ONDAAAAAAAAAAAAAAAAAAAAAAAAAA¡!", nombre, "!")
    a = 123
    print(type(a))
    salu2(a)

# Funcion con muchos argumentos
def muchos_saludos(*nombres):
    """Esta funcion saluda a todos los que desees."""
    i = 0
    print("hola", end="")
    while len(nombres) > i:
        # Ultimo nombre
        if i == len(nombres) - 1:
            print(nombres[i])
        else:
            # Cualquier otro nombre
            print(nombres[i], end=", ")
        i += 1

muchos_saludos("Nicole", "Luis", "otros estudiantes")

# Funcion greet con argumentos de keyword
def greet(firstname, lastname):
    print('hello', firstname, lastname)

# Llama funcion con argumentos en desorden
greet(lastname='jobs', firstname='pabel')

# Funcion con argumentos desconocidos
def greet(**person):
    """Persona tiene caracteristica firstname y lastname"""
    print('hello', person['firstname'], person['lastname'])

greet(firstname='pabel', lastname='jobs')
greet(lastname='jobs', firstname='pabel')
greet(firstname='bill', lastname='Gates', age=55) # Se puede pasar mas parametros

# Funcion con valores por defecto
def greet(name='guest'):
    print('hello', name)

greet()  # Utiliza el valor dado de antemano
greet('stevie')

# Funcion con resultado
def suma(a, b):
    return a + b

# Programacion funcional
# Se pueden usar funciones dentro de funciones
total = suma(5, suma(10, 20))
print(total)

# Calculo lambda
x_al_cuadrado = lambda x: x * x
a1 = x_al_cuadrado(5)
print(a1)

# Lambda de varias variables
suma = lambda x1, x2, x3: x1 + x2 + x3
print(suma(99, 98, 97))

sumas = lambda *x: x[0] + x[1] + x[2] + x[3]
print(sumas(100, 200, 300, 400))

# Uso de la funcion anonima
print((lambda x: x * x)(6))  # Funcion anonima

name = 'stevie'
def greet():
    global name
    name = 'bill'
    print('hello', name)

greet()

