#Cortázar Tinajero Luis Enrique........
#Uso de reducciones (colapsar resultados)

#Multiplicacion de todos los numeros en la lista


from functools import reduce

bigdata = [2,3,5,7,11,13,19,23,29]

#función x*y..............
# . .      .       .          .          .     .

multiplicar = lambda x,y: x*y
suma = lambda x,y: x+y



print(reduce(multiplicar,bigdata))
print(reduce(suma,bigdata))


