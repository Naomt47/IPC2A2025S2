from ListaDoble import ListaDoble


newList = ListaDoble()
#id, nombre, direccion, antiguedad, sucursales
newList.agregarPrimero(1, "Banrural","Zona 9", 26, 100)
newList.agregarPrimero(2, "Industrial", "Zona 21", 5, 20)
newList.agregarPrimero(3, "G&T", "Zona 2", 10, 45)
newList.agregarUltimo(4, "Promerica","Zona 7", 8, 14)


newList.eliminar(1)
newList.recorrer()

newList.graficar()