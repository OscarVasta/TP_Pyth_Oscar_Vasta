
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

    def __init__(self, dividendo, divisor, entero=0):
        self.dividendo = dividendo
        self.divisor = divisor

    def __str__(self):
        return "fracción:(%i/%i)" % (self.dividendo, self.divisor)

    def __add__(self, otra):
        suma_dividendo = (self.dividendo * otra.divisor) + (otra.dividendo * self.divisor)
        suma_divisor = self.divisor * otra.divisor
        return Fraccion(suma_dividendo, suma_divisor)

    def __sub__(self, otra):
        resta_dividendo = (self.dividendo * otra.divisor) - (otra.dividendo * self.divisor)
        resta_divisor = self.divisor * otra.divisor
        return Fraccion(resta_dividendo, resta_divisor)

    def __mul__(self, otra):
        multiplica_dividendo = self.dividendo * otra.dividendo
        multiplica_divisor = self.divisor * otra.divisor
        return Fraccion(multiplica_dividendo, multiplica_divisor)

    def simplificar(self):
        if self.dividendo > self.divisor:
            test = self.divisor
        else:
            test = self.dividendo
        for i in range(1, test):
            if self.dividendo % i == 0 and self.divisor % i ==0:
                mcd = i
            else:
                entero = mcd
                nuevodivisor = self.divisor / i
                nuevodividendo = self.dividendo / i
                return entero, nuevodivisor, nuevodividendo



#---------------------------------------------------------
cociente = Fraccion(50, 60)
print('a) ',cociente)
a = Fraccion(50, 60)
b = Fraccion(20, 30)
c = a + b
print('b) suma ',a,'+',b,'=', c, end='')

d = a - b
print ('c) resta',a,'-',b,'=', d,'   ( sin simplificación )')
e = a * b
print ('d) multiplica',a,'x',b,'=', e,'   ( sin simplificación )')
