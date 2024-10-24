  





class A:
    
    _a:float=0.0
    _b:float=0.0
    _c:float=0.0


    def _init_(self ,a:float,b:float,c:float):
  	self.a = a
	self.b = b
	self.c = c

    


class B:
    _d:float=0.0
    _e:float=0.0
    def _init_(self,d:float,e:float)
 	self.d = d
	self.e = e
     def sumar_todo(self,aa:float, bb:float):
	x:float=self.d+self.e+aa+bb
	return x
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





