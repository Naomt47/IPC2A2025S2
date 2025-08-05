from Clases.Empleado import Empleado
from Clases.Persona import Persona

def Menu():
    print("------------------ MENU PRINCIPAL ------------------")
    print("1. Registrar Persona")
    print("2. Registrar Empleado")
    print("3. Mostrar Informacion")
    print("4. Opción Administrador")
    print("5. Salir")
    print("---------------------------------------------------")



if __name__ == "__main__":
    #Guardar Objetos
    listado = []


    while True: 
        Menu()

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            edad = input("Ingrese el edad: ")


            personaCreada = Persona(nombre, edad)
            listado.append(personaCreada)
            print("Persona Creada con exito!")


        elif opcion == "2":
            nombre = input("Ingrese el nombre: ")
            edad = input("Ingrese el edad: ")
            salario = input("Ingrese el salario: ")

            empleadoCreado = Empleado(nombre, edad, salario)
            listado.append(empleadoCreado)

            print("Empleado Creado con exito!")

        elif opcion == "3":
            print("IMPRESION DE DATOS:")

            for elemento in listado: 
                print(elemento.nombre, elemento.edad)
                if isinstance(elemento, Empleado):
                    print(elemento.salario)

                print("")
        elif opcion == "4":
            print()
            print("OPCION ADMINISTRADOR")


            print("Ingrese su usario y contraseña: ")
            user = input("Usuario: ")
            password = input("Contraseña: ")


            if user == "admin" and password == "1234": 
                print("Bienvenido Administrador")

                print()

                if len(listado) == 0:
                    print("No hay registros")

                else: 
                    for obj in listado: 
                        if isinstance(obj, Empleado):
                            userEmp = input(f"Ingrese el usuario para {obj.nombre}: ")
                            obj.serUserEmployee(userEmp)
                            print("Asignación correcta")
                            print(obj.getUserEmployee())

            else: 
                print("usuario o contraseña incorrecta")

        elif opcion == "5":
            break

        else: 
            print("Opción no valida, Ingresa otra opción")

