#Cortázar Tinajero Luis Enrique ......


from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario




#s3 hijo de RepositorioDeUsuarios..............

class S3(RepositorioDeUsuarios):
    __clientId: str
    __secretkey: str
    __bucket: str

    def __init__(mi, clientId: str, secretkey: str, bucket: str):
        mi.__clientId = clientId
        mi.__secretkey = secretkey
        mi.__bucket = bucket



    def abrir(mi) ->None:
        print(f"Estableciendo conexión a AW S3 {mi.__clientId}:{mi.__secretkey}")

    def guardar(mi, usuario:Usuario) -> None:
        userData = {"nombre": usuario.getNombre(),
                    "apellido":usuario.getApellido(),
                    "edad": usuario.getEdad() }
        print(f"Guardando usuario de la bandeja:{mi.__bucket}: {userData}")

    def cerrar(mi) -> None:
        print("Cerrando conexión AW S3")
        
