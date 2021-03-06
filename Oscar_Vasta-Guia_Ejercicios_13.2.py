"""
Oscar_Vasta-Guia_Ejercicios_13.2
Agregar a ListaEnlazada un método append que reciba una ListaEnlazada y
agregue a la lista actual los elementos que se encuentran en la lista recibida.
"""
class Nodo:
    def __init__(self, nombre=None, DNI=None, sig=None):
        self.nombre = nombre
        self.DNI = DNI
        self.sig = sig
    def __str__(self):
        return "%012s : %8d" %(self.nombre, self.DNI)
#
class listasimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    def append(self, elemento):
        if self.cabeza == None:
            self.cabeza = elemento

        if self.cola != None:
            self.cola.sig = elemento
            self.cola = elemento

        self.cola = elemento
#
    def show(self):
        aux = self.cabeza
        while aux != None:
            print (aux)
            aux = aux.sig
            
    def extend(self,lext):
        ls.cola.sig=lext.cabeza

#····································································································#
#creamos 2 array con datos iniciales para la 1º lista simple
nombres = ['Oscar', 'Graciela', 'Mecedes', 'Sara', 'Gise', 'Matias', 'Alexis', 'Ezequiel','Estanislao']
documentos =[12602584, 12856585, 34569876, 41876543, 29887021, 40987656, 93567876, 39876656, 6986501]
#creamos 2 array con datos iniciales para la 2º lista simple
nombres1 = ['Mauro', 'Ulices', 'Torcuato']
documentos1 =[41567987, 32004987, 989043]
#Cargamos los array en la 1º lista enlazada
ls = listasimple()
for i in range(len(nombres)):
    nod = Nodo(nombres[i], documentos[i])
    ls.append(nod)
#listamos lo que cargamos en la 1º lista
print("LISTA ENLAZADA EXISTENTE:\n")
ls.show()
#Cargamos los array en la 2º lista
ls1 = listasimple()
for i in range(len(nombres1)):
    nod = Nodo(nombres1[i], documentos1[i])
    ls1.append(nod)
#listamos lo que cargamos en la 2º lista
print("OTRA LISTA:")
ls1.show()

# Damos la opcion de unir las 2 listas o salir
while(True):
    print()
    print("** OPCIONES **\n"+"U. unir otra lista a lista existente / O. Terminar\n")
    opc = input("Ingrese la Opción: ")
    opcion = opc.lower()
    if opcion == "u":
        ls.extend(ls1)
        print("Y EL RESULTADO DE AGREGARLE LA OTRA LISTA A  LA LISTA EXISTENTE ES:")
        ls.show()
    elif opcion == "o":
        break

# ----------------------------- E.O.F. ---------------------------------
