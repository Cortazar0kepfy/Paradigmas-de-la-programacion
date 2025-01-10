#Cortázar Tinajero Luis Enrique


from aplicacion.banco.cliente_bancario import ClienteBancario

# Asegúrate de que cliente esté definido antes de los bloques try-except
cliente = None

try:
    cliente = ClienteBancario("Jaime Lozano", "La Mañaeca", 28, 0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())
except Exception as e:
    print("Error: " + str(e))

# Este bloque try-except captura cualquier error al intentar acceder a __nombres
try:
    print(cliente.__nombres) 
except Exception as ex:
    print("Error: " + str(ex))

# Forma correcta de acceder a nombres
if cliente is not None:
    print(cliente.nombres)
else:
    print("Error: cliente no está definido.")

