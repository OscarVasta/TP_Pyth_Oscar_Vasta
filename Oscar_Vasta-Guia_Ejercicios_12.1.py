"""
Oscar_Vasta-Guia_Ejercicios_12.1.

a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
instantes de tiempo (números enteros expresados en segundos), con la condición desde
< hasta.
b) Implementar el método duracion que devuelve la duración en segundos del intervalo.
    (en caso que el período de teiempo este invertido , calcula la amplitud del período
     a la inversa para que el resultado de la amplitud del tiempo de un resultado absoluto)
c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo intervalo
    resultante de la intersección entre ambos, o lanzar una excepción si la intersección
    es nula.(el método interseccion devuelve 2 parámetros , el 1º es el intervalode tiempo de
    intersección y el 2º es un string de aviso si el período se encuentra fuera del entorno o
    es nulo si los entornos se interceptan)
d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adyacentes
    ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo
    intervalo resultante de la unión entre ambos. (el método union devuelve 2 parámetros , el 1º es
    la suma de los tiempos de los 2 períodos y el 2º es un string de aviso si el período se
    encuentra fuera del entorno)
"""
# a)
class intervalo:
    # constructor
    def __init__(self, desde, hasta):
        """
        :param desde: un número entero representado en segundos
        :param hasta: un número entero representado en segundos mayor a desde
        """
        assert desde < hasta, "desde debe ser menor que hasta"
        # atributos de instancia
        self._desde = desde
        self._hasta = hasta

        def get_desde(self):
            return self._desde

        def get_hasta(self):
            return self._hasta
# b)
        def duracion(self):
            return self._hasta - self._desde

# c)
    def interseccion(self, otro_intervalo):
        # [] ()
        # [(])
        # ([)]
        i2_desde = otro_intervalo.get_desde()
        i2_hasta = otro_intervalo.get_hasta()
        hasta = self.get_hasta()
        desde = self.get_desde()
        if hasta > i2_desde and hasta <= i2_hasta:
            # [()] o ([)]
            if desde <= i2_desde:
                # ([)]
                return Intervalo(i2_desde, hasta)
            else:
                # [()]
                return Intervalo(desde, hasta)
        else:
            # [] ()
            # [(])
            if desde > i2_desde and desde <= i2_hasta:
                # [(])
                return Intervalo(desde, i2_hasta)
            else:
                raise ValueError("No hay interseccion entre intervalos")

# d)
    def union(self, intervalo_union):
        def interseccion(self, otro_intervalo):
            # [] ()
            # [(])
            # ([)]
            i3_desde = intervalo_union.get_desde()
            i3_hasta = intervalo_union.get_hasta()
            hasta = self.get_hasta()
            desde = self.get_desde()
            if hasta > i3_desde and hasta <= i3_hasta:
                # [()] o ([)]
                if desde <= i3_desde:
                    # ([)]
                    return intervalo(desde, i3_hasta)
                else:
                    # [()]
                    return Intervalo(i3_desde, i3_hasta)
            else:
                # [] ()
                # [(])
                if desde > i2_desde and desde <= i2_hasta:
                    # [(])
                    return Intervalo(i3_desde, hasta)
                else:
                    raise ValueError("No hay interseccion entre intervalos")


        
#------------------ E.O.F. ------------------------------------------------------
