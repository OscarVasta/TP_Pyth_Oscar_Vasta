
"""
Oscar_Vasta-Guia_Ejercicios_12.2.

a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
asignan en el constructor, y se imprimen como X/Y en el método __str__.

b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
con la suma de ambas.

c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción
con el producto de ambas.

d) Crear un método simplificar que modifica la fracción actual de forma que los valores
del dividendo y divisor sean los menores posibles.
"""
class Fraccion:
    dividendo=0
    divisor=0
    def __init__(self, dividendo, divisor):
        self._dividendo = dividendo
        self._divisor = divisor

    def __str__(self):
        return "(%i/%i)" % (self._dividendo, self._divisor)

    def __add__(self, otra):
        suma_dividendo = self.dividendo + otra.dividendo
        suma_divisor = self.divisor + otra.divisor
        return Fraccion(suma_dividendo, suma_divisor )
#---------------------------------------------------------
cociente = Fraccion(50, 60)
print(str(cociente))
a = Fraccion(50, 60)
b = Fraccion(20, 30)
#c= a + b
#print(str(c))
print(a + b)
