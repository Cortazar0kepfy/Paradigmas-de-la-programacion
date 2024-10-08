#===================================================================================
#Cortazar Tinajero Luis Enrique.


#Mi primera funcion
def saludo():
    #Documentacion rapida de la funcion
    """Esta funcion saluda"""
    print('priviet, como estas?')
   #====================
   #llamado de funcion
   #===========
   saludo()
   #========
   #se ejecuta pero no se asigna
   #===========
   salida = (salida)
   #======
   #Mostrar documentacion
   #==========
   #help(saludo)
   #===============
   

   #=========================================================
   #funcion argumento
   #=================================================
   def salu2(nombre):
       """Esta funcion te saluda por tu nombre"""
       print("QUE ONDAAAAAAAAAAAAAAAAAAAAAAAAAA¡!",nombre,"!")
       saludos("Cortaziano")
       a = 123
       print(type(a))
       saludos(a)


#=======================================
#funcion con muchos argumentos
#===================
def muchos_saludos(*nombres):
    """ esta funcion saluda a todos los que desees."""
    i = 0
    #==============================================
    #es para ponerlo de corrido
    #===========================================
    print("hola", end="")
    while len(nombres)> i:
        #ultimo nombre
        if (i==len(nombres)-1):
            print(nombres[i])
        else:
            #cualquier otro nombre
            print(nombres[i], end=",")
            i+=1
muchos_saludos("Nicole, luis and another students")

def greet(firstname, lastname):
    print('helo', firstname, lastname)


#=========================================================
#llama funcion con argumentos en desorden
#=============================================
greet(lastname='jobs', firstname='pabel')

#========================================
#funcion con argumentos desconocidos**
#=============================
def greet(**person):
    #=======================================
    #persona tiene caracteristica firstname y lastname
    #===============================================
    print('hello', person['firstname'], person['lastname'])

greet(firstname='pabel', lastname='jobs')
greet(lastname='jobs', firstname='pabel')
greet(firstname='bill', lastname='Gates', age=55) #se puede pasar mas parametros,



#===============
#funcion con valores por defecto
#============================
def greet(name = 'guest'):
    print('hello', name)

greet()  #utiliza el valor dado de antemano
greet('stevie')

#===========
#funcion con resultado
#=======
def suma(a, b):
    return a+b


#===================
#programacion funcional
# se pueden usar funciones dentro de funciones
#=====
total=suma(5, suma(10,20))
print(total)



#==========================================================
#calculo lambda
#================
x_al_cuadrado = lamda  x : x * x
a1 = x_al_cuadrado(5)
print(a1)


#============
#lambda de varias variaaables
#=====================
suma = lambda x1, x2, x3:x1+x2+x3
print(suma(99,98,98))

sumas = lambda *x:x[0]+x[1]+x[2]+x[3]

print (sumas(100, 200, 300, 400))



#=========================
#uso de la funcion annima
#=================================

print((lambda x: x*x(6)   #funcion anonima
    name = 'stevie'
    def greet():
    global name 
    name = 'bill'
    print('helo',name)

    greet()



  

