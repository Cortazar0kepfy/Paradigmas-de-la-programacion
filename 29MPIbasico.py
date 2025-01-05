#Cortázar Tinajero Luis Enrique-







# Importar la biblioteca mpi4py
from mpi4py import MPI

# Crear un objeto comunicador
comunicadores = MPI.COMM_WORLD

# Obtener el número total de procesos
n_procesos = comunicadores.Get_size()

# Obtener el identificador de este proceso
quien_soy = comunicadores.Get_rank()

# Imprimir un saludo desde cada proceso
print("Saludos desde el proceso", str(quien_soy), "de", str(n_procesos))

# Si este proceso es el proceso 0, hacer esto:
if quien_soy == 0:
    print("Yo soy el proceso 0")

# Si este proceso es el proceso 1, hacer esto otro:
elif quien_soy == 1:
    print("Yo soy el proceso 1")

# Si este proceso no es ni el 0 ni el 1, hacer esto:
else:
    print("Yo no soy ninguno de los dos primeros procesos")

