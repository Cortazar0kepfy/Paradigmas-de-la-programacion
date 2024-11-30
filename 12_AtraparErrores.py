#Cortázar Tinajero Luis Enrique..........




from aplicacion.Banco.Cliente_Bancario import ClienteBancario



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
print('cliente'.'nombres')


































