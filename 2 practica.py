thisdict =	{
  "Fisica": "5",
  "Historia": "8",
  "Matematicas": "10",
}
print(thisdict)
# Diccionario con los créditos de las asignaturas
asignaturas = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}

# Inicializar el contador de créditos totales
total_creditos = 0#Aqui inicia a contar los creditos prof

# Mostrar los créditos de cada asignatura
for asignatura, creditos in asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos")
    total_creditos += creditos

# Mostrar el número total de créditos del curso
print(f"Número total de créditos del curso: {total_creditos}")
