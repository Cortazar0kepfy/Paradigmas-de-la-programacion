#Cortázar Tinajero Luis Enrique........()()()()()
#Clase cCcCCCCCCcLIENTEBANCARIO............CcccccCCCCcccccc<<<<<<<<<<<<<<iiii






#Cortázar Tinajero Luis Enrique ...........     #Clase cliente bancario..................
#Perteneciente como segunda parte de" atrapar errores(number:12)
# . - - - - - - - - - - -   - - - - - l- -   
#En el directorio:Rusalkakkka;cd:aplicación,cd:banco...........................................(i)
#Distinto a los que hay en @Paradigmas-de-la programación............(contenido vacío referencial...)






class ClienteBancario:
    __nombres:str = None
    __apellidos:str = None
    __edad:int = 0
    __balanceDeCuenta:float = 0.0


    def __init__(self, nombre:str, apellidos:str, edad:int=0, balanceDeCuenta:float=0.0):
        self.__validarEdad(edad)
        self.nombres = nombres
        self.apellidos = apellidos
        self.__edad = edad
        self.balanceDeCuenta = balanceDeCuenta

    def getNombreCompleto(self) -> str:
        return self.nombres + "" + self.apellidos

    def __mandarEmail(self, titulo:str, texto:str) ->None:
        print("Mandar Email: " + titulo + "con texto: " + texto)

    def __enviarBalanceAlBanco(self, cantidad:float) -> None:
        print("Enviando cantidad: " + str(cantidad) + "al banco......")
#Método privado con dos guiones bajos
# Si la edad es menor que 18 genera un error
#()()()()()()()()()()()()()()(()()()


    def __validarEdad(self, edad:int) ->None:
        if edad < 18:
            raise Exception("Es menor de edad")

    def imprimirInfo(self) -> str:
        return "Nombre: " + self.getNombreCompleto() + ", Edad: ", + str(self.__edad) + ",Balance: " + str(self.__BalanceDeCuenta)





#Método privado que checa si el balance es negativo
#   y genera un error..



    def __validarCantidad(self, balanceDeCuenta:float) ->None:
        if balanceDeCuenta < 0:
            raise Exception("El balance en la cuenta no puede ser negativo")

    def guardarDinero(self, balanceDeCuenta:float) ->None:
        self.__balanceDeCuenta = self.__balanceDeCuenta + cantidad
        self.__mandarEmail("------ guardando déposito -----", "se recibieron " + str(cantidad))
        self.__enviarBalanceAlBanco(cantidad)

    def retirarDinero(self, cantidad:float) -> None:
        cantidadFinal = self.__balanceDeCuenta - cantidad
        self.__validarcantidad(cantidadfinal)
        self.__validarCantidad(CantidadFinal)
        self.__balanceDeCuenta = cantidadFinal
        self.__mandarEmail("-------Retirando dinero-------", " se retira " + str(cantidad))
        self.__enviarBalanceAlBanco(cantidad)



