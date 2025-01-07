# Cortázar Tinajero Luis Enrique.

from mpi4py import MPI
import numpy

# Enviar objeto mensajero con comunicación bloqueada
# (cada proceso espera a que le reciban su mensaje)

class Mensaje:
    def __init__(self, rank):
        self.x = range(rank*10)
        self.p = "vengo del proceso " + str(rank)

# Programa principal
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    s = Mensaje(rank)

    # Que te mande el anterior y si es cero que sea el último
    fuente = rank-1 if rank != 0 else size-1

    # Mándalo al siguiente y si eres el último mándalo al primero     
    destino = rank+1 if rank != size-1 else 0

    # Send y recv son operaciones bloqueadas y generan que el 
    # código se atore esperando que alguien reciba un mensaje
    # esto se resuelve enviando con los pares y recibiendo con los impares
    if rank % 2 == 0:
        comm.send(s, dest=destino)
        m = comm.recv(source=fuente)
    else:
        m = comm.recv(source=fuente)
        comm.send(s, dest=destino)

    print("Soy el proceso ", rank, ", el resultado es ", len(m.x), ", ", m.p)

    # Para una comunicación más rápida se utilizan arreglos de numpy
    # send y recv van con mayúscula y cambian un poco
    # Se indica el tipo de datos explícitamente

    # Ejemplo 1 usando enteros
    if rank == 0:
        data = numpy.arange(10, dtype='i')
        comm.Send([data, MPI.INT], dest=1, tag=77)
    elif rank == 1:
        data = numpy.empty(10, dtype='i')
        comm.Recv([data, MPI.INT], source=0, tag=77)
        print(data)

    # También se puede indicar el tipo de dato
    # pero deben coincidir en el tipo de arreglos a los extremos del mensaje
    if rank == 0:
        data = numpy.arange(10, dtype=numpy.float64)
        comm.Send(data, dest=1, tag=13)
    elif rank == 1:
        data = numpy.arange(10, dtype=numpy.float64)
        comm.Recv(data, source=0, tag=13)
        print(data)

