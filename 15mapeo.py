#Cortázar Tinajero Luis Enrique..............


#LMA


#función pura x**2
#()()()()()()()()(


def alcuadrado(x):
    return x*x
#función pura x**3
def alcubo(x):
    return x*x*x
# .                     .                        .          .                       .       .     .                   .
# .                    .                         .             .             .            .       . . .
#Mapeo de una función pura......()()()()()()()()
def mapeo(func, lista_numeros):
    resultado = []


    for i in lista_numeros:
        resultado.append(func(i))

    return resultado


cuadrados = mapeo(alcuadrado,[2,5,2,3.8,1.2,6.6,1j,7,8])
cubos = mapeo(alcubo,[1,2,3,4,5,6,7,8])
print(cuadrados)
print(cubos)


#Funciones dentro de funciones()()()(()()()()()()()()())
def en_mayuscula(texto):
    return texto.upper()


def en_minuscula(texto):
    return texto.lower()

def saludar(func):
    saludo = func("Hola,¿Cómo estás? " )
    print(saludo)





#Con strings()()()()()()()()()()()()(
saludar(en_mayuscula)
saludar(en_minuscula)

#Funciones abstractas dentro de funciones...................()
# . . . .                     .        .      .              .



def divisor(x):
    def dividiendo(y):
        return y/x
    return dividiendo



#Primero generamos la función y/2
#    -
division = divisor(2)
#La usamos pues para calcular 3/2<<<<<<<<<<<<<<<<<<<<<:
print(division(3))





#Uso de la función map con una lista..........



#Lista de ciudades y su temperatura


temps =[("Berlin", 8), ("Cairo", 14), ("Buenos Aires", 22), ("Los Angeles", 17), ("Tokyo", 18), ("Nueva York", 8),("Londres",2), ("Pekin", 32), ("México Tenochtitlan", 21)]






C_a_F = lambda datos: (datos[0], (9/5)*datos[1] + 32)
print(list(map(C_a_F, temps)))





  
