#Cortázar Tinajero Luis Enrique................
#................................
#                       .....LMA...ESFM...

#importaciones............................
# :
# :




import numpy as np
from Curva import Curva,zspline
import matplotlib.pyplot as plt
import math
#===============================================================================////////////////////////
#   Conjunto de puntos./
#    ...  número de puntos ..

nump:np.int32 = 8
#dimensión......
dim:np.int32 = 2
#Memoria para puntos

puntos = np.zeros(dim*nump,dtype=np.float64)
#          Parametrización. . . . . .  . . . . . . . .. . .  . 
X =np.linspace(0.0*np.pi,nump+1)     ## Generar valores equidistantes entre 0 y 2π.
#Genera nump + 1 puntos equidistantes en el intervalo [0,2π][0, 2\pi]. 
#Matemáticamente, esto significa que se esta dividiendo el intervalo:
# [0,2π][0, 2\pi]en partes iguales.

#Caracterizando a la coordenada x:

puntos[0:nump] = np.cos(X[0:nump]) + 0.0*np.sin(2*X[0:nump])
#Caracterizando a la coordenada y:

puntos[nump:2*nump] = np.sin(X[0:nump]) + 0.0*np.sin(2*X[0:nump])

#=========================================================================

#Curva Z-spline de n puntos z-spline(p,d,n,m)
# p: puntos, d: dimensión, n: segmento de curva , m: continuidad.
#Es decir:

#Este código está configurado para trabajar con un conjunto de puntos en un espacio 2D utilizando librerías de Python como NumPy y Matplotlib. 
n:np.int32 = 1000
x1,y1 = zspline(puntos,dim,n,2)
x2,y2 = zspline(puntos,dim,n,1)
x3,y3 = zspline(puntos,dim,n,0)
plt.plot(x3,y3,lw=3,color="orange")
plt.plot(x2,y2,lw=3,color="red")
plt.plot(x1,y1,lw=3,color="blue")
plt.scatter(puntos[0:nump],puntos[nump:2*nump],marker='o',color='black')
plt.xlabel("coordenada x")
plt.ylabel("coordenada y")
plt. title("Curva cerrada z-zspline en 2D")
plt.show()

            







