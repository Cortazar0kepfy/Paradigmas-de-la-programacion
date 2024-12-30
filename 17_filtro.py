#Cortázar Tinajero Luis Enrique.......



#Modulo de estadística.........


import statistics

bigdata = [1, 3, 2.7, 0.8, 4.3, -0.1]
promedio = statistics.mean(bigdata)
print("Promedio:", promedio)

# Hazme una lista de elementos que cumplan la condición x > promedio
print(list(filter(lambda x: x > promedio, bigdata)))

# Limpiar los datos
paises = {"", "Argentina", "", "Brasil", "", "Chile", "", "México", "", "Cuba", "", "Venezuela"}

# Filtra lo que no contiene nada
print(list(filter(None, paises)))

