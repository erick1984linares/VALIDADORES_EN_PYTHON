#ejercicio 2: calcular el area lateral de un prisma
area_lateral_de_un_prisma, perimetro_de_la_base, arista=0.0, 0.0, 0.0
#asignacion de valores
perimetro_de_la_base=12
arista=3
#calculo
area_lateral_de_un_prisma=(perimetro_de_la_base*arista)
#mostrar valores
print("perimetro de la base=", perimetro_de_la_base)
print("arista=", arista)
print("area lateral de un prisma=", area_lateral_de_un_prisma)
area_lateral_minima=(area_lateral_de_un_prisma<36)
print("es area lateral minima", area_lateral_minima)
