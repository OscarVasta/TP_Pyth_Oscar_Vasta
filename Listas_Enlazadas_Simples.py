"""
listas enlazadas simples
"""
class Nodo:
    def __init__(self, nombre=None, cedula=None, sig=None):
        self.nombre = nombre
        self.cedula = cedula
        self.sig = sig
    def __str__(self):
        return "%s %s" %(self.nombre, self.cedula)
class lsimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    def agregar(self, elemento):
        if self.cabeza == None:
            self.cabeza = elemento

        if self.cola != None:
            self.cola.sig = elemento
            self.cola = elemento

        self.cola = elemento

    def listar(self):
        aux = self.cabeza
        while aux != None:
            print(aux)
            aux = aux.sig

# creamos un Switch
if __name__ == "__main__":
    ls = lsimple()
    while(True):
        print("----Menu----\n"+
            "1. Agregar\n"+
            "2. Listar\n")
        num = input("Ingrese la Opción")
        if num == "1":
            nombre = input("Ingrese el nombre")
            cedula = input("Ingrese la caedula")
            nod = Nodo(nombre, cedula)
            ls.agregar(nod)
        elif num == "2":
            ls.listar()
