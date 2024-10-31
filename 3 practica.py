print(" ")
print("Angel Andrey Muñoz Centeno 3W")
print("ESTE ES MI EXAMEN")
print(" ")
# Lista de materias o asignaturas
asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

# Diccikonario para almacenar las calificaciones 
notas = {}

# Preguntar al alumnno por la nota de cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota que has sacado en {asignatura}: "))
    notas[asignatura] = nota

# Mostrar las notas por pantalla
for asignatura, nota in notas.items():
    print(f"En {asignatura} tu calif es: {nota}")
