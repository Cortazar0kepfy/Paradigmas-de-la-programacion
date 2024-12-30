#Cortazar Tinajero Luis Enrique...

# Tres listas.........///////////////


mi_lista = [1,2,3]
tu_lista = (10,20,30)
su_lista = (40,50,100)


#función multiplicar*2


def multiplicar_por2(elemento):
    return elemento*2



#función que filtra pares.......()()()()()((

def solo_impar(elemento):
    return elemento % 2 !=0

# .       . lista de pares de datos de las dos listas...<>>>>
# . .         .zip sirve para jugar listas....
# - . . . . . . . . . . . 
#   list es para que la haga toda lista........




print(list(zip("a", "b", "c", "b", "d", "m", "n")))



una_lista = ["a", "b", "c", "b", "d", "n", "n", "n"]



#Crear conjunto de elementos que se repiten....()()()

duplicados = set[x for in una_lista if una_lista.count(x) > 1]
print(duplicados)
#     # .   ."!"

#Expresión generadora.....
# Contiene un iterador
# !!!!00000_Contiene un iterador   ."
#Range(5) es un iterador de 0 a 4.............
cuadrados = (x*x for x in range(5))



#Next llama a la siguiente evaluación del iterador


print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
                            
#Pasar una función generadora........
import math


# suma de elementos del iterador
print(sum(x*x for in range(5)))

#Lista de comprehensión pasada como función
#   .       Arma la lista por usar[]
numeros_pares = [x for in range(21) if x%2 == 0]
print([x for x in range(21) if x%2 == 0])
print(numeros_pares)




























