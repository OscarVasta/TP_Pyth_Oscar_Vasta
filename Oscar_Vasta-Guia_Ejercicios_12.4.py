
"""
Oscar_Vasta-Guia_Ejercicios_12.4.

Escribir una clase Caja para representar cuánto dinero hay en una caja de un
negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:
>>> c = Caja({500: 6, 300: 7, 2: 4})
ValueError: Denominación "300" no permitida
16
>>> c = Caja({500: 6, 100: 7, 2: 4})
>>> str(c)
'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
>>> c.agregar({250: 2})
ValueError: Denominación "250" no permitida
>>> c.agregar({50: 2, 2: 1})
>>> str(c)
'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
>>> c.quitar({50: 3, 100: 1})
ValueError: No hay suficientes billetes de denominación "50"
>>> c.quitar({50: 2, 100: 1})
200
>>> str(c)
'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'


billeper ={}
billetes ={}
billeper = {1: 0, 5: 0, 10: 0}
a={1: 15, 2: 8}
billetes = a
print(len(billetes))
for i in billetes:
    if i in billeper:
        print(i * billetes[i])
    else:
        print(i,"no existe esa denominación")
"""
#define un diccionario con las denominaciones válidas solo para
# validar de forma indexada , el 2º término del diccionario se deja en 0 por qu e no se usa
denominaciones={1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}
class Caja:
    def __init__(self, arqueo):
        #arqueo es un diccionario que contiene denominaciones y cantidad de billetes existentes en la caja
        self.arqueo = arqueo
    def __str__(self):
            #intenta verificar si la denominacion esta entre las denominaciones permitidas en el array "billeper
        totalcaja = 0
        for i in self.arqueo:
            try:
                if i in denominaciones:
                    totalcaja +=  i * self.arqueo[i]
                else:
                    raise ValueError('Denominación '+i+' no existe')
            except  ValueError as e:
                    return(e)
        return 'Caja '+str(self.arqueo)+' total: '+str(totalcaja)+' pesos'


#------------------- PRUEBA ----------------------------------------
c = Caja({500: 6, 100: 7, 2: 4})
print(c)
print('_'* 80,'\n')

#---------------------E.O.F.----------------------------------------
