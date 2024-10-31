#Cortazar Tinajero Luis Enrique.

#Matemática de Algoritmos.
#    .
#    .
#    .
#clase computadora
# . . . . . . . . . . . . . . 


class Persona:
    nombres: str = None
    apellidos: str = None
    edad: int = 0
    direccion: str = None
    computadora: Computadora = None

    # Constructor de persona
    def __init__(self, nombres: str, apellidos: str, edad: int, direccion: str, marca: str, capacidad: int, ram: int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.computadora = Computadora(marca, capacidad, ram)
        print(f"---Accedimos al constructor de la persona: {nombres} {apellidos}")

    def imprimirInfo(self) -> None:
        print(f"---Mi nombre es {self.nombres} {self.apellidos}, tengo {self.edad} años")
        self.computadora.imprimirInfoPC()


class Persona:
    nombres: str = None
    apellidos: str = None
    edad: int = 0
    direccion: str = None
    computadora: Computadora = None

    # Constructor de persona
    def __init__(self, nombres: str, apellidos: str, edad: int, direccion: str, marca: str, capacidad: int, ram: int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.computadora = Computadora(marca, capacidad, ram)
        print(f"---Accedimos al constructor de la persona: {nombres} {apellidos}")

    def imprimirInfo(self) -> None:
        print(f"---Mi nombre es {self.nombres} {self.apellidos}, tengo {self.edad} años")
        self.computadora.imprimirInfoPC()

def funcion1():
    persona1 = Persona("Carlos", "Perez", 30, "Atizapan", "Lenovo", 700, 8)
    print("\n")
    persona1.imprimirInfo()
    print("\n")

    persona2 = Persona("Magdalena", "Contreras", 87, "La hermosa Juárez", "IBM", 200, 4)
    print("\n")
    persona2.imprimirInfo()
    print("\n")

# Llamar a la función1.....
funcion1()










































































    













































































    --

    -

 -




















   































   


















