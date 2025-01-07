#Cortázar Tinajero Luis Enrique......


from mpi4py import MPI
import numpy

#Objeto comunicador
comm = MPI.COMM_WORLD


#Quiensoy

rank = comm.Get_rank()


# El proceso 0 tiene datos y los otros no

if rank  == =0:
    data = {'key1' : [7, 2.72, 2+3],
            'key2' : ('abc', 'xyz')}
else:
    data = None

#Enviar diccionario a todos los procesos desde root

data = comm.bcast(data, root=0)
print(data)



n = 10
if rank == 0:

    data = numpy.arange(n, dtype='i')
else:
    data = numpy.empty(n, dtype= 'i')


comm.Bcast([data,MPI.INT], root=0)



for i in range(n):
    assert data[i] == i
print(data)
