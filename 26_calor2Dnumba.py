#Cortázar Tinajero Luis Enrique
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplt3d import Axes 3D
from matplotlib import cm
import time
from numba import jit


n = np.array([512,512])

L = np.array([1.0,1.0])

k = 0.2
pasos = 1000

dx = L/n
udx2 = 1.0/(dx*dx)
dt = 0.25*(min(dx[0],dx[1]**2)/k
print("dt = ",dt)
nt = n[0]*n[1]
print("celdas = ",nt)


u = np.zeros(nt,dtype=np.float64)
un = np.zeros(nt,dtype=np.float64)
           
