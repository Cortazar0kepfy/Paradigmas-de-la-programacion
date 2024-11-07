  
#Cortázar Tinajero Luis Enrique...........................
#. #.





class A:
    __a:float=0.0
    __b:float=0.0
    __c:float=0.0

    def __init__(self,a:float,b:float,c:float):
        self.a = a
        self.b = b
        self.c = c
#===============================================================================================================
#La clase B tiene dos números reales..............................
#==============================

class B:
    __d:float=0.0
    __e:float=0.0

    def __init__(self,d:float,e:float):
        self.d = d
        self.e = e


#===========<><>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#Método "sumar todo"(internos + externos)
#=============================================================
    def sumar_todo(self, aa:float, bb:float):
        x:float=self.d+self.e+aa+bb
        return x




#Asociación.............................><<<<<<<<<<<<<<<<<<<<<<<<>><>>>><>>>><<<>>
#usando objetos independientes......................................
#><><><<<<><><><><><>>
objetoA = A(1.0,2.0,3.0)
objetoB  B(4.0,5.0)
print(objetoB.sumar_todo(objetoA.a,objetoA.b))


#El objeto C tiene dos reales y un "objeto A"...........<><><><><><><><><><><><><<<<><><
#El objeto A se instancia dentro de C.......................<><><><><><><><><><><><><><><><>
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

class C:
    __d:float=0.0
    __e:float=0.0
    __Aa:A=None
    
    def __init__(self,d:float,e:float):
        self.d = d
        self.e = e
        #........<><><><>A está isntanciada..........................<>
        #...................adentro...............................
        self.Aa = A(1.0,2.0,3.0)

    def __init__


    def sumar_todo(self):
        x:float=self.d+self.e+self.As.a+self.Aa.b
        return x 



#Composición.........................
#contiene otro objeto dentro.........................

objetoC = C(4.0,5.0)
print(objetoC.sumar_todo())


class D:
    __d:float=0.0
    __e:float=0.0
    __Aa:A=None

    def __init__(self,d:float,e:float,Aa:A):


#Agregación.......
#====================================================================
#Construye el objeto agregrado
objetoD = D(4.0,5.0,objetoA)
print(objetoD.sumar_todo())

    

    


  
   


   







    



  
   
    
        
       
 	




#Asociacion.............
objetoA = A(1.0,2.0,3.0)
objetoB = B(4.0,5.0)
print(objetoB.sumar_todo(objetoA.a,objeto.b))


class C:
    _d:float=0.0
    _e:float=0.0
    _Aa:A=None
    def _init_(self,d:float,e:float):
	self.d = d
	self.e = e
	self.Aa = A(1.0,2.0,3.0)
    def sumar_todo(self):
	x:float=self.d+self.e+self.Aa.a+self.Aa.b
	return x



#composicion...............



objetoC = C(4.0,5.0)
print(objetoC.sumar_todo()) 


class D:
    _d:float=0.0
    _e:float=0.0
    _Aa:A=None
    
    def _init_(self,d:float,e:float,Aa:A):
	self.d = d
	self.e = e
	self.Aa = Aa
    def sumar_todo(self):
	x:float=self.d+self.e+self.Aa.a+self.Aa.b
	return x


#Agregacion..........................
objeto D = D(4.0,5.0,objetoA)
print(objetoD.sumar_todo())

	x:float=self.d+self.e+self.Aa.a+self





