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
class intervalos:
    # constructor
    def __init__(self, desde1=0, hasta1=0, desde2=0, hasta2=0):
        """
        :param desde: un número entero representado en segundos
        :param hasta: un número entero representado en segundos mayor a desde
        """
        assert desde1 < hasta1, "desde debe ser menor que hasta"
        # atributos de instancia
        self.desde1 = desde1
        self.hasta1 = hasta1
        self.desde2 = desde2
        self.hasta2 = hasta2

        def muestra_intervalo(self):
            muestra = ("Desde {} segundos  hasta {} segundos") #Mensaje
            print(muestra_intervalo.format(self.desde1, self.hasta1)) #Usamos
# b)
        def duracion(self):
            return self.hasta1 - self.desde1

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





#------------------ E.O.F. ------------------------------------------------------
a = intervalos(23654, 23789)
print(intervalos.duracion())
