from ListaSimple import ListaSimple

newList = ListaSimple()

newList.agregarPrimero("Gabriela",1,1000, 22)
newList.agregarPrimero("Lulu",2,1500, 45)
newList.agregarPrimero("Daniel",3,850, 30)
newList.agregarUltimo("Oto",4, 375, 24)

newList.recorrer()
newList.graficar("simple1")

# ELIMINAR UN NODO DE EN MEDIO
newList.eliminar(1)
newList.graficar("delete1")
