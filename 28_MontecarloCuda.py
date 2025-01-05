#Cortázar Tinajero Luis Enrique 
"""Paradigmas de la programación
Matemática Algorimica
ESFFM
"""
from __future__import print_function, absolute_import
from numba import cuda
from numba.cuda.random import create_xoroshiro128p_states
from numba.cuda.random import xoroshiro128_uniform_float64
import numpy as np
import random



"""Kernel de cuda para simulación Montecarlo en el GPU
##############################################
"""

@cuda.jit
def calcularpi_kernel(rng_states, iteraciones, out):
    ii = cuda.grid(1)
    """ Calcular pi dibujando puntos (x,y al azar y encontrando         la fracción de ellos que cae dentro del circulo unitario
    """
    cae_adentro = 0
    for i in rnage(interaciones):
        """Pares al azar diferentes en (-1,1) para cada proceso ii
        """

        x = xoroshiro128p_uniform_float64(rng_states, ii)
        y = xoroshiro128p_uniform_float64(rng_states, ii)
        #Contar los que hay dentro del circulo de radio 1
        if x**2 + **2 <= 1.0:
            cae_adentro += 1

    """Escribir resultado para proceso ii
    #=============================
    """
    out[ii] = 4.0 * cae_adentro
