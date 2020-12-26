"""
Practica_Programacion_Orientada_a_Objetos.py
por Oscar_Vasta
"""
class humano:
    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion

    def presentar(self):
        presentacion = ("Hola soy {}, mi edad es {} y mi ocupación es {}")
        print(presentacion.format(self.nombre, self.edad, self.ocupacion))

Persona1 = humano(31, "Pedro", "Desocupado")

Persona1.presentar()

class intervalo:
    def __init__(self, desde, hasta):
        self.desde = desde
        self.hasta = hasta


    def duracion(self, desde, hasta ):
        return self.hasta - self.desde


Persona1 = humano(31, "Pedro", "Desocupado")

Persona1.presentar()
Periodos = intervalo(27345, 27999)
Duracion = intervalo.duracion(27345, 27999)
