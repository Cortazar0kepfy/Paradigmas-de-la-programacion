#Cortázar Tinajero Luis Enrique...........
#      LMA.


#clase computadora.........
class Computadora:
    marca: str = None
    capacidad: int = 0
    ram: int = 0






#Constructor.....................

    def __init__(self, marca:str, capacidad:int, ram:int):
        print("Accediendo al constructor de la pc:{marca}")
        self.marca = marca
        self.capacidad = capacidad
        self.ram = ram

    def imprimirInfoPC(self):
        print(f"Está es la Computadora marca: {self.marca} con amacenamiento de {self.capacidad y memoria de {self.ram}GB")

#   .Destructor.......................
    def __del__(self):
        print(f"Se eliminó la computadora: {self.marca"}



#.....Clase Persona
class Persona:
    nombres: str = None
    apellidos: str = None
    edad: int = 0
    direccion: str = None
    computadora: Computadora = None

#Constructor de persona...................

    def __init__(self,nombres:str, apellidos:str, edad:int, direccion:str, marca:str, capacidad:int, ram:int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.Computadora = Computadora(marca, capacidad, ram)
        print(f"---Accedimos al constructor de la persona: {nombre {apellidos}")

    def imprimirInfo(self) -> None:
        print(f"--Mi nombre es {self.nombres} {self.apellidos},tengo {self.edad} años de edad, vivo en {self.dirección} ")
        
        self.Computadora.imprimirInfoPC()


#Destructor
    def __del__(self):
        print(f"---Eliminamos a la persona... {self.nombres} {self.apellidos}")



#función 1 es el programa...........................
def funcion1():
    persona = Persona("Carlos","Perez","40","Xochimilco","Lenovo",700,8)
    print("\n")
    persona.imprimirInfo()
    print("\n")
    persona2= Persona("Magdalena","Carrillo",35,"Jalapa","IBM",200,4)
    print("\n")
    persona2.imprimirInfo()
    print("\n")
#:::::::::::::::::::::::::::::::::::::::::::::::::::

#Llamar a función1

#:::::.............................................

funcion1()


