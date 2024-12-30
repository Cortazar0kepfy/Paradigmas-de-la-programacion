#Cortazar Tinajero Luis Enrique...

# Tres listas.........//////////////


import statistics

bigdata = [1, 3, 2.7, 0.8, 4.3, -0.1]
promedio = statistics.mean(bigdata)
print("Promedio:", promedio)

# Crear una lista de elementos que cumplen la condición x > promedio
print(list(filter(lambda x: x > promedio, bigdata)))

# Limpiar los datos
paises = {"", "Argentina", "", "Brasil", "", "Chile", "", "México", "", "Cuba", "", "Venezuela"}

# Filtra lo que no contiene nada
print(list(filter(None, paises)))

# Tres listas
mi_lista = [1, 2, 3]
tu_lista = [10, 20, 30]
su_lista = [40, 50, 100]

# Función multiplicar por 2
def multiplicar_por2(elemento):
    return elemento * 2

# Función que filtra impares
def solo_impar(elemento):
    return elemento % 2 != 0

# Lista de pares de datos de las tres listas
print(list(zip(mi_lista, tu_lista, su_lista)))

# Crear conjunto de elementos que se repiten
una_lista = ["a", "b", "c", "b", "d", "n", "n", "n"]
duplicados = set(x for x in una_lista if una_lista.count(x) > 1)
print(duplicados)

# Expresión generadora
cuadrados = (x * x for x in range(5))

# Next llama a la siguiente evaluación del iterador
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))

# Suma de elementos del iterador
print(sum(x * x for x in range(5)))

# Lista de comprensión pasada como función
numeros_pares = [x for x in range(21) if x % 2 == 0]
print(numeros_pares)

