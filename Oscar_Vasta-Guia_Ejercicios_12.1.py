"""
Oscar_Vasta-Guia_Ejercicios_12.1.

a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
instantes de tiempo (números enteros expresados en segundos), con la condición desde
< hasta.
    **Si el intervalo enviado tubiera un tiempo desde mayor devuelve un assertError alertándolo.**

b) Implementar el método duracion que devuelve la duración en segundos del intervalo.

c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo intervalo
    resultante de la intersección entre ambos, o lanzar una excepción si la intersección
    es nula.
        **Si el período enviado no tiene continuidad con el 1º períod la funcion interseccion() devuelve un ValueError alertándolo.**

d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adyacentes
    ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo
    intervalo resultante de la unión entre ambos.
        **Si el período enviado no tiene continuidad con el 1º períod la funcion union() devuelve un ValueError alertándolo.**
"""
# a)
class Intervalo:
    # Atributos o propiedades
    desde = 0
    hasta = 0
    #interpreto que al poner los atributos en 0 , le estoy indicando que es un número entero, no ?

    # constructor
    def __init__(self, desde, hasta):
        # atributos de instancia
        assert desde < hasta, "desde debe ser menor que hasta"
        self.desde = desde
        self.hasta = hasta



# b)
    def duracion(self):
        return self.hasta - self.desde

"""
# c)
    def interseccion(self):
        # [] ()
        # [(])
        # ([)]

        if self.hasta1 > self.desde2 and self.hasta1 <= self.hasta2:
            # [()] o ([)]
            if self.desde1 <= self.desde2:
                # ([)]
                return Intervalo(self.desde2, self.hasta1)
            else:
                # [()]
                return Intervalo(self.desde1, self.hasta1)
        else:
            # [] ()
            # [(])
            if self.desde1 > self.desde2 and self.desde1 <= self.hasta2:
                # [(])
                return Intervalo(self.desde1, self.hasta2)
            else:
                raise ValueError("No hay interseccion entre intervalos")

# d)
    def union(self):
            # [] ()
            # [(])
            # ([)]
            if self.hasta1 > self.desde2 and self.hasta1 <= self.hasta2:
                # [()] o ([)]
                if self.desde1 <= self.desde2:
                    # ([)]
                    return Intervalo(self.desde1, self.hasta2)
                else:
                    # [()]
                    return Intervalo(self.desde2, self.hasta2)
            else:
                # [] ()
                # [(])
                if self.desde1 > self.desde2 and self.desde1 <= self.hasta2:
                    # [(])
                    return Intervalo(self.desde2, self.hasta1)
                else:
                    raise ValueError("No hay interseccion entre intervalos")
"""




#----------------------------------------------------------------
intervalo1=Intervalo(23654, 23789)
intervalo2=Intervalo(0, 112)
intervalo3=Intervalo(480, 498)
intervalos=[intervalo1, intervalo2, intervalo3]

for interv in intervalos:
        print(interv.duracion())




#------------------------ E.O.F. --------------------------------
