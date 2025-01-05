#Cortázar Tinajero Luis Enrique.

"""OJo !!! Para correr se escribe:
    mpiexec -n 4 python3 27_mpibasico.py
   
   Pero si quieres más procesos que procesadores
   mpirun --oversubscribe  -n 400 pyhton3 27_mpibasico.py

   Para correr en cuatro procesos.
"""

from mpi4py import MPI

"""Crear un objeto comunicador
#===============================
"""
comunicadores = MPI.COMM_WORLD


"""Número Total de procesos
"""
n_procesos = comunicadores.Get_size()


"""Identificador de esté proceso
"""

quien_soy = comunicadores.Get_rank()

print("Saludos desde el proceso ", str(quien_soy), "de",str(n_procesos))

#Si yo soy el cero hago esto:

if quien_soy ==0:
    print("Yo soy el proceso 0")

#Si yo soy el uno hago esto otro


elif quien_soy ==1:
    print("Yo soy el proceso 1")


"""Si yo no soy el uno ni el dos hago esto
"""

else:
    print("Yo no soy ninguno de los dos primeros proceso")



