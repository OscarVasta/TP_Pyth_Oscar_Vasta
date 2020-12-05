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
for billetes in billeper:
    try:
        if billetes in billeper[billetes]:
            total = (total + billetes[billeper]*billetes)
            print('$',total)
        else:
            raise ValueError(str(billetes)+ "No existe esa denominación")
    except ValueError as e:
        print(e)
"""
