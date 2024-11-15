#Cortázar Tinajero Luis Enrique..........


#La clase ClienteBancario está en el subdirectorio
#   aplicación/banco/



# Cortázar Tinajero Luis Enrique..........

# La clase ClienteBancario está en el subdirectorio
# aplicación/banco/

from aplicacion.banco.cliente_bancario import ClienteBancario


# try: intenta (correr las instrucciones)
# except: atrapar el error en una variable e
# se puede convertir a string

# Error por sacar más dinero del que tiene......

try:
    cliente = ClienteBancario("Jaime Andrade", "Hernández Sánchez", 28, 0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())

# Exception es el objeto más general de error
except Exception as e:
    print("Error: " + str(e))

# ()()()()()()()()()()()()()()()

try:
    print(cliente._ClienteBancario__nombres)  # Accediendo a un atributo privado
except Exception as ex:
    print("Error: " + str(ex))

# Forma correcta......
print(cliente.nombres)  # Accediendo a un atributo público, si existe
































