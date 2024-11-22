#Cortázar Tinajero Luis Enrique.............()()()(()()()()()()())(
from aplicacion.modelos.usuario import Usuario




#Desarrollo de la clase manejodeinscripciones.......
#No tiene variables!!!!!!!!!!!!!!!

class ManaejoDeInscripciones:
    #Decorador staticmethod
    #El objeto solo tiene la función inscribirUsuario
    #Envuelve la función sin llamar variables locales..............
    # El objeto ManejoDeInscripciones es la interface intercambiable....
    #@staticmethod................[][][][][][][][][][][[][][][][][][][]
    
    def inscribirUsuario(usuario:Usuario, repositorioDeUsuarios: RepositoriosDeUsuarios ) -> None:
        print("--------Guardando Usuario-----------\n")
        repositoriosDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
        
