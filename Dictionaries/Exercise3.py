#we create a dictionary of students
estudiantes = {}

while True:
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1} del estudiante: "))
        notas.append(nota)
    estudiantes[nombre] = {"notas": notas}
    estudiantes[nombre] = {"notas": notas, "promedio": sum(notas)/len(notas)}

print("Notas de los estudiantes:")
for estudiante in estudiantes:
    print(f"{estudiante}: {estudiantes[estudiante]['notas']}")
print()

print("Promedio de notas de los estudiantes:")
for estudiante in estudiantes:
    print(f"{estudiante}: {estudiantes[estudiante]['promedio']}")
print()

promedio_general = sum([estudiantes[estudiante]['promedio'] for estudiante in estudiantes])/len(estudiantes)
print(f"Promedio general de la clase: {promedio_general}")
