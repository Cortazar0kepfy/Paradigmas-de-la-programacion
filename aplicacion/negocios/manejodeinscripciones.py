#Cortázar Tinajero Luis Enrique.............()()()(()()()()()()())(
from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios




#Desarrollo de la clase manejodeinscripciones.......
#No tiene variables!!!!!!!!!!!!!!!

class ManejoDeInscripciones:
    #Decorador staticmethod
    #El objeto solo tiene la función inscribirUsuario
    #Envuelve la función sin llamar variables locales..............
    # El objeto ManejoDeInscripciones es la interface intercambiable....
    #@staticmethod................[][][][][][][][][][][[][][][][][][][]
    @staticmethod
    def inscribirUsuario(usuario:Usuario, repositorioDeUsuarios:RepositorioDeUsuarios) -> None:
        print("--------Guardando Usuario-----------\n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
        
