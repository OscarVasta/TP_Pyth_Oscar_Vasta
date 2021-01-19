"""
Oscar_Vasta-Guia_Ejercicios_13.3
Ejercicio 13.3. Implementar el método remover_todos(elemento) de ListaEnlazada, que recibe
un elemento y remueve de la lista todas las apariciones del mismo, devolviendo la cantidad
de elementos removidos. La lista debe ser recorrida una sola vez.
"""
class Nodo:
    def __init__(self, nombre=None, DNI=None, siguiente=None):
        self.nombre = nombre
        self.DNI = DNI
        self.siguiente = siguiente
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
            self.cola.siguiente = elemento
            self.cola = elemento

        self.cola = elemento
#
    def show(self):
        aux = self.cabeza
        while aux != None:
            print (aux)
            aux = aux.siguiente

    def extend(self,lext):
        ls.cola.siguiente=lext.cabeza

    def remover_todosnom(self, nombrerm):
        actual = self.cabeza
        siguiente = self.cabeza.siguiente
        c_borrados = 0


        while actual != None:
            if actual.nombre != nombrerm:
                actual = actual.siguiente
            else:
                siguiente = actual.siguiente
                actual.siguiente = None
                actual = siguiente
                c_borrados += 1
        return c_borrados
    
    def remover_todos(self, elemento):
        anterior = None
        actual = self.cabeza
        c_borrados = 0

        while actual != None:
            if actual.nombre != elemento.nombre and actual.dni != elemento.dni:
                anterior = actual
                actual = actual.siguiente
            else:  # lo borro de la lista
                if anterior is None:  # entonces era la cabeza de la lista
                    self.cabeza = actual.siguiente
                if actual.siguiente is None:  # entonces era la cola de la lista
                    if anterior is not None:
                        anterior.siguiente = None
                    self.cola = anterior  # si anterior es None la lista queda vacía
                if anterior is not None:  # borro el nodo entrelazando el anterior con el siguiente
                    anterior.siguiente = actual.siguiente
                c_borrados += 1
        return c_borrados


#····································································································#
#creamos 2 array con datos iniciales para la 1º lista simple
nombres = ['Oscar', 'Graciela', 'Mecedes', 'Sara', 'Gise', 'Matias', 'Alexis', 'Ezequiel','Estanislao']
documentos =[12602584, 12856585, 34569876, 41876543, 29887021, 40987656, 93567876, 39876656, 6986501]
#creamos 2 array con datos iniciales para la 2º lista simple
nombres1 = ['Mauro', 'Ulices', 'Torcuato', 'Oscar']
documentos1 =[41567987, 32004987, 989043, 45908745]
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
    print("** OPCIONES **\n"+"U. unir otra lista a lista existente / R. Remover u Nombre / O. Terminar\n")
    opc = input("Ingrese la Opción: ")
    opcion = opc.lower()
    if opcion == "u":
        ls.extend(ls1)
        print("Y EL RESULTADO DE AGREGARLE LA OTRA LISTA A  LA LISTA EXISTENTE ES:")
        ls.show()
    if opcion == "r":
        inombre=input("Ingrese nombre: ")
        borrados = ls.remover_todosnom(inombre)
        print("Cantidad de registros borrados: ",borrados)
        ls.show()
    elif opcion == "o":
        break

# ----------------------------- E.O.F. ---------------------------------
