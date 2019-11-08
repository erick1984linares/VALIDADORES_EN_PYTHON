#area lateral de un prisma cuadrangular regular
area_lateral,perimetro,altura,lado=0.0,0.0,0.0,0.0

#asignacion de valores
altura=6
lado=3

#calculos
perimetro=(lado*4)
area_lateral=(perimetro*altura)

#mostrar resultados
print("la base de un prisma es un cuadrado y el valor de su lado es:",lado,"m")
print("el perimetro de la base cuadrangular es:",perimetro,"m")
print("la altura del prisma es:",altura,"m")
print("el valor del area lateral del prisma es:",area_lateral,"metros cuadrados")

#verificador 10
grande=area_lateral>70
print("Es el area lateral grande:",grande)
