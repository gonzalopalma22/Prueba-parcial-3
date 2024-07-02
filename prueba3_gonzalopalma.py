import json
import os
archivo_datos = "registroalumnos.txt"

def cargar_datos():
    if os.path.exists(archivo_datos) and os.path.getsize(archivo_datos) > 0:
        with open(archivo_datos, 'r') as file:
            try:
                datos = json.load(file)
            except json.JSONDecodeError:
                datos = {}
    else:
        datos = {}
    return datos
def guardar_datos(datos):
    with open(archivo_datos, 'w') as archivo:
        json.dump(datos, archivo, indent=4)


def registro_alumno():
    nombre = input("Nombre alumno: ")
    apellido = input("Apellido: ")
    matematica = float(input("Ingrese nota de Matematicas: "))
    ciencias = float(input("Ingrese nota de Lenguaje: "))
    historia = float(input("Ingrese nota de Historia: "))

    promedio = (matematica + historia + ciencias)/3

    
    alumno = {
        'nombre': nombre,
        'apellido' :apellido,
        'matematica': matematica,
        'ciencias' :ciencias,
        'historia': historia,
        'promedio': promedio
    }
    datos = cargar_datos()

    datos[nombre] = alumno
    guardar_datos(datos)

    print("Alumno registrado correctamente")

def buscar_alumno():
    print(f"Buscar alumno por nombre: ")
    buscar_nombre = input("Ingrese el nombre del alumno al que desea encontrar: ")
    datos = cargar_datos()
    if buscar_nombre in datos:
        alumno = datos[buscar_nombre]
        print("\nDatos del alumno:")
        print(f"Nombre: {alumno['nombre']} {alumno['apellido']}")
        print(f"Nota Matemáticas: {alumno['matematica']}")
        print(f"Nota Ciencias: {alumno['ciencias']}")
        print(f"Nota Historia: {alumno['historia']}")
        print(f"Promedio: {alumno['promedio']}")
    
    else:
        print(f"No se encontro ningun alumno con ese nombre '{buscar_nombre}'.\n")



def mostrar_lista_alumnos():
    print("\nLista de alumnos registrados:")
    
    datos = cargar_datos()
    
    if datos:
        for alumno in datos.values():
            print(f"{alumno['nombre']} {alumno['apellido']} - Promedio: {alumno['promedio']:.2f}")
    else:
        print("No hay ningun alumno registrado.\n")
    
def main():
    while True:
        print("\nBienvenido al sistema de registro de notas escolares")
        print("1. Registrar alumno")
        print("2. Buscar alumno por nombre")
        print("3. Mostrar lista de estudiantes")
        print("4. Salir del programa")

        opcion = input("\nSeleccione su opción: ")

        if opcion == "1":
            registro_alumno()
        elif opcion == "2":
            buscar_alumno()
        elif opcion == "3":
            mostrar_lista_alumnos()
        elif opcion == "4":
            print("Gracias por usar el sistema de registro de alumnos. ¡Hasta luego!")
            break
        else:
            print("Opción ingresada no existe, ingrese números del 1 al 4")

if __name__ == "__main__":
    main()