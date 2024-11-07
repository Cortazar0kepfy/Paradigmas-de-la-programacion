#Cortázar Tinajero Luis Enrique...........


#Programación Orientada a Objetos.......

#Una clase para un objeto vacío 
#.No está tan vacío, necesita la palabra pass = pasar.
#====================================================
class Objetovacio:
    pass
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#nada es la instanciación de la clase objeto vacío
#))))))))))))))))))))))))))))))))
nada = Objetovacio()
print(type(nada))



#la clase llanta..............)))))
#(((((((((((((((((((((((((((((((((((((((((((
class Llanta:
    cuenta = 0
    
    def __init__(mi,radio=50,ancho=30,presión=1.5):
        #variable de la estructura completa Llanta
        Llanta.cuenta += 1
        #variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presión = presión











   
   

    
  




#objetos instanciados

llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presión=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((


#Objeto que contiene a otros objetos

class Coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1,llanta2,llanta3,llanta4)


print("total de llantas:",Llanta.cuenta)
print("Presión de la llanta 4 = ",llanta4.presión)
print("Radio de la llanta 4 = ",llanta4.radio)
print("Radio de la llanta 3 = ",llanta3.radio)
print("Presión de la llanta 1 de mi choche = ",micoche.llanta1.presión)



#Encapsulamiento.........................

#Uso de la función de python property para poner y obtener atributos
#    a variables protegidas con __
#==================================================================================



class Estudiante:
    def __init__(mi):
        mi.__nombre = ''
    def ponerme_nombre(mi, nombre):
        print('se llamó a ponerme_nombre')
        mi.__nombre = nombre
    def obtener_nombre(mi):
        print('se llamó a obtener_nombre')
        return mi.__nombre
    nombre=property(obtener_nombre,ponerme_nombre)






#Crear objeto estudiante sin nombre 
estudiante = Estudiante()
#Ponerle nombre usando la propiedad nombre y el método ponerme_nombre.
#Sin tener que llamar explícitamente ala función obtener_nombre.

estudiante.nombre = "Diego"

#Obtener el nombre con el método obtener_nombre
#    __nombre es una variable encapsulada(no visisble desde fuera.)
#Sin tener que llamar explicitamente a la función obtener_nombre............

print(estudiante.nombre)

#Esto no funciona.......
#     print(estudiante.__nombre)




#Herencia de clases................................

class Cuadrilatero:
    def __init__(mi,a,b,c,d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d

    def perimetro(mi):
        p=mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
        print("perimetro=",p)
        return p

#Su hijo rectángulo
#Rectángulo es hijo de cuádrilatero...........
class Rectangulo(Cuadrilatero):
    def __init__(self, a, b):

#Constructor de su madre...................................
        super().__init__(a, b, a, b)

#Su nieto cuadrado.....
#   Hijo de Rectángulo............


class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area



#Crear un cuadrado
#(((((((((((((((((((((((((((((((((((((((((((((((((((

cuadrado1 = Cuadrado(5)

#Llamar al método perimetro de su abuelo Cuadrilatero
perimetro1 = cuadrado1.perimetro()


#Llamar a su propio método de área
area1 = cuadrado1.area()

print("Perimetro = ",perimetro1)
print("Area = ", area1)

