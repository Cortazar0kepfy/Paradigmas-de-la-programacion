#Cortázar Tinajero Luis Enrique  >>> >       > stdio.h ja!



from mpi4py import MPI 
import numpy



comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank+1)**2
#Manden sus datos al . . . . . proceso root=0 ( en orden)

datas = comm.gather(data, root=0)
"""Asegurarse de que todo funcione
"""
if rank == 0:
    for i in range(size):
        assert datas[i] == (i+1)**2
else:
    assert datas is None
    print(datas)

#Ahora más rápido con numpy
n = 10
# Arreglos de ceros de tamaño n
#Sumando con un escalar (en cada entrada)

sedarray = numpy.zeros(n, dtype='i')+rank
recvrarray = None
if rank == 0:
    #Matriz vacía de tamaño de procesos *n
    #dtype es el tipo de dato (i9 es entero
    recvarray = numpy.empty([size, n], dtype='i')

#Gather es rápido para numpy
#Enviar datos al proceso root"""""
comm.Gather(sedarray, recvarray, root=0)
if rank == 0:
    for i in range(size):
        #Revisar por fila la matriz
        # : significa todos los elementos de esa dimensión
        # allclose es un métdo de numpy que compara los elementsos
        assert numpy.allclose(recvarray[i, :], i)
print(recvarray)




