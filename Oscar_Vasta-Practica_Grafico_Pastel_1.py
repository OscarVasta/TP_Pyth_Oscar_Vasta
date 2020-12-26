"""
Oscar_Vasta-Practica_Grafico_Pastel.py
PROGRAMA DE EJEMPLO PARA HACER UN GRÁFICO DE PASTEL CON PYHON USANDO MATPLOLIB Y PYPLOT
"""
from matplolib import pyplot
#-- unos datos de ejemplo ficticios para graficar
lenguajes = ('Python','C','Java','Go','JavaScript')
slices = (100, 130, 90, 80, 128) # valor arbitrario asignado a cada porcion a representar
colores = ('red', 'blue' ,'green', 'DD98AA', '#18492D') #color asignado a cada porcion
valores = (0.1, 0, 0, 0) #para que la 1º porcion aparezca separada
pyplot.rcParams['toolbar'] = 'None' # para que no muestre la barra de herramientas al pie del grafico
#------------------------------------------------
# se usa la funcion pyplot.pie() pasandole los diversos parámetros pero
# se le antepone la variable texto y se lo itera en for tex para que lo repita
#
_, _, texto = pyplot.pie(slices, colors=colores, labels=lenguajes, autopct='%1.1f%%',
                        explode=valores, startangle=90)
#--- esto se hace para que le asigne color blanco a cada una de los rotulos de las porciones
for text in texto:
    text.set_color('white')
#
pyplot.axis('equal') # para que el pastel se vea circular , si no se ve ovalado
pyplot.title('Grafica de Lenguajes de Programación')
#-- las 2 sigientes instrucciones son para que la asignacion de colores quede como
#-- una tabla de referencias a la derecha del pastel , en este caso no se uso
#pyplot.legend(labels=lenguajes)
#pyplot.show
#-------------------------------------------------------------------------------
pyplot.savefig('lenguajes.png') #para que esto guarda el grafico en una archivo
# E.O.F.
                  
