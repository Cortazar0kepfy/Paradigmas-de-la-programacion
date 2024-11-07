#Cortázar Tinajero Luis Enrique..................
#LMA.................

#Condicionales.......
#La sentencia if se usa para ejecutar un bloque de código si se cumple una condición.





precio = 50


#sentencia:
if precio < 50:
    print("Algo anda mal es menor a  50 :( ")


elif precio > 50:
    print("El precio es mayor a 50 :(  ")


else:
    print("El precio es 50   (:   ")


precio = 50
cantidad = 5
total = precio*cantidad



#Condicionales Anidados
#                            .Puedes anidar sentencias if dentro de otras sentencias if.


if total > 100:
    if total > 500:
        print("Total es mayor que 500 :(  ")

    else:
        if total < 500 and total > 400:
            print("Total es menor que 500 pero mayor que 400")
        elif total < 500 and total > 300:
            print("Total entre 300 y 500")
        else:
            print("total entre 100 y 300")

#Condicional de igualdad son ==
#==========================================================

elif total == 100:
    print("total es 100")
else:
    print("total menor que 100")


#Contador hasta que la condición sea verdaera....
#===========================================================================================
num = 0
while num < 5:
    num = num + 1
    print('num = ', num)

num = 0
while num < 5:
    num += 1
    print('num = ', num)
    if num == 3:
        break


num = 0
while num < 5:
    num += 1
    if num > 3:
        continue
    print('num = ',num)


#bucle sobre lista
nums = [ 10,20,30,40,50]
for i in nums:
    print(i)


#bucle sobre string.....
for char in 'hola':
    print(char)


#bucle sobre diccionario
#items = elementos
#==========================================
numeros = {1:'uno', 2: 'dos', 3: 'tres'}
for par in numeros.items():
    print(par)

#bucle sobre diccionario.
#key = llave
#value = valor
#)))))))))))))))))))))))))))))))))))))))))))))
for k,v in numeros.items():
    print("key = ", k , ", value =", v)


