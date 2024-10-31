print(" ")
print("Angel Andrey Muñoz Centeno 3W")
print(" ")
# Crer un diccionario para almacenar la información del usario
usuario = {}

# Preguntar al usuario por su información
usuario['nombre'] = input("Ingrese su nombre: ")#pedir su nombre
usuario['edad'] = input("Ingrese su edad: ")#pedir du edad
usuario['direccion'] = input("Ingrese su dirección: ")#pedir su direccion
usuario['telefono'] = input("Ingrese su número celular: ")#pedir su telefono

# Mostrar lo anterior o la info
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")
