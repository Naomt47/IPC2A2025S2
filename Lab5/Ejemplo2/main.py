from Juego.Juego import JuegoTotito

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n--- Menú del Juego de Totito ---")
    print("1. Cargar configuración con minidom")
    print("2. Cargar configuración con ElementTree")
    print("3. Jugar")
    print("4. Salir")

def main():
    juego = JuegoTotito()
    configCargada = False
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            if juego.cargarConfiguracionMinidom("C:/Users/marroquin/Documents/Universidad/2025/Auxiliatura/Semestre2/Clases/Lab 4/Ejemplo2/Archivos/config.xml"):
                print("Configuración cargada exitosamente con minidom")
                configCargada = True
            else:
                print("No se pudo cargar la configuración")
        
        elif opcion == "2":
            if juego.cargarConfiguracionElemenTree("C:/Users/marroquin/Documents/Universidad/2025/Auxiliatura/Semestre2/Clases/Lab 4/Ejemplo2/Archivos/config.xml"):
                print("Configuración cargada exitosamente con ElementTree")
                configCargada = True
            else:
                print("No se pudo cargar la configuración")
        
        elif opcion == "3":
            if not configCargada:
                print("Primero debes cargar una configuración")
                continue
            
            ganador = juego.jugar()
            
            # Preguntar si desea guardar el resultado
            guardar = input("¿Deseas guardar el resultado? (s/n): ").lower()
            if guardar == "s":
                print("1. Generar Resultado con minidom")
                print("2. Generar Resultado con ElementTree")
                metodo = input("Selecciona el método: ")
                
                if metodo == "1":
                    juego.generarResultadoMinidom("C:/Users/marroquin/Documents/Universidad/2025/Auxiliatura/Semestre2/Clases/Lab 4/Ejemplo2/Archivos/resultadoMiniDom.xml", ganador)
                elif metodo == "2":
                    juego.generarResultadoElementTree("C:/Users/marroquin/Documents/Universidad/2025/Auxiliatura/Semestre2/Clases/Lab 4/Ejemplo2/Archivos/resultadoElemntTree.xml", ganador)
                else:
                    print("Opción inválida")
            
            # Preguntar si desea jugar de nuevo
            jugar_nuevo = input("¿Deseas jugar de nuevo? (s/n): ").lower()
            if jugar_nuevo != "s":
                break
            
            # Resetear el juego
            juego = JuegoTotito()
            configCargada = False
        
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()