#Cortázar Tinajero Luis Enrique 
#LMA..................
#En este programa se va a tomar el álgebra de conjuntos(Teoría Cantoriana),ósea las operaciones entre otros objetos
#       de estudio en python(diccionarios)
even_nums = {2,4,6,8,10}     #Aqui representa la forma par de la expresión 2k para un "k" ordinario.
print(even_nums)


#El bool es un concepto asociado al "álgebra booleana",pues podemos decir que even_nums = {2k}
#  así , veamos pues que el bool no es parte del conjunto

emp = {1,"Stevie",10.5, True}  #conjunto de diferentes objetos.............
print(emp)

nums = {1,2,2,3,4,4,5,5}
print(nums)


#Convertir secuencia a conjunto
#No lo genera en orden


s = set('hola')
print(s)

s = set((1,2,3,4,5))
print(s)                #tupla a conjunto........................






#De diccionario a conjunto    : conjunto de llaves

d = {1:'uno',2:'dos'}
s= set(d)
print(s)



s.add(100)
print(s)


s.update(nums)
print(s)



s1={1,2,3,4,5}
s2={4,5,6,7,8}



su = s1|s2       #La unión de conjuntos "AUB"    
print(su)



si = s1&s2      #Intersección de conjuntos
print(si)




sr = s1-s2  #diferencia de conjuntos........
print(sr) 


sp = s2-s1
print(sp)


ss = s1^s2                  #diferencia simétrica...............

#     .
#     -
#
#
#

#Uso de diccionarios.............

#Son una estructura de datos fundamental, es decir es un conjunto de pares clave-valor.
#Permiten almacenar y manipular datos de manera "flexible",ya que pueden contener diferentes tipos
# de datos.









capitales = {"USA":"Washington D.C.","France":"Paris","India":"New Delhi"}
print(capitales)





#llave:valor.

#diccionario vacio.

d = {}



#llave entera,valor string.
numeros={1:"uno",2:"dos",3:"tres"}


#llave real valor string
decimales={1.5:"uno y medio",2.5:"dos y medio",3.5:"tres y medio"}

#llave tupla valor string
cosas={("Parker","Reynolds","Camlin"):"pluma", ("LG","Samsung","Whirpool"):"refrigerador"}


#llave string valor int
romanos = {'I':1,'II':2,'III':3,:4,'V':5,"VI":6,"VII":7}
print(romanos)
print(romanos["I"])

print(capitales.get("India"))
print(capitales.get("india"))


#Reportar llave y valor.............................

for k in capitales:
    print("key = " + k + ", value = " + capitales[k])




#Nuevo dato para el diccionario..........................................

capitales["Mexico"] = "CDMX"
print(capitales)


#borrar dato del diccionario
del capitales["Mexico"]
print(Capitales)


#borrar todo del diccionario...................
del capitales


#Reportar llaves
print(romanos.keys())

#Reportar valores
print(romanos.values())


#Juicio de llave (está o no está en el diccionario)
print("I" in romanos)
print("X" in romanos)
print("XX" in romanos)














