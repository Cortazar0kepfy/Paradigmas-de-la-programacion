#Cortázar Tinajero Luis Enrique.
#Interface...........

#Del directorio aplicacion  el subdirectorio repositorio,
# archivo basededatos.py : trae el onjeto BaseDeDatos.
from aplicacion.repositorio.basededatos import BaseDeDatos




from aplicacion.repositorio.s3 import S3




from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos




from aplicacion.modelos.usuario import Usuario


from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones



#Creando el objeto usuario
usuario = Usuario("Roberto", "Jimenez",18)


#Creando el objeto s3.............()()()()()()()()()()()()()()(()()()(
repositorios3 = S3("321321321", "sdf324223", "MiCubeta")




#Proceso de Interface..............................()()()()()()()()()()()()()()()()()()()()()()()()

ManejoDeInscripciones.inscribirUsuario(usuario,repositorios3)
print("\n")

#Crea el objeto SistemaDeArchivos...........
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")



ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")


#Crea el objeto basedatos.......-----------
repositorioBaseDeDatos = BaseDeDatos("localhost", "admin", "admin123")



ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")


