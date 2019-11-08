#INPUT
nombre_del_profesor=input("ingrese el nombre del profesor:")
sueldo=int(input("ingrese el sueldo:"))
descuendo_por_afp=int(input("ingrese el descuento por afp:"))
gastos_mesuales=int(input("ingrese gastos mensuales:"))

#PROCESSING
total=(sueldo - descuendo_por_afp - gastos_mesuales)

#VERIFICADOR
profesor_satisfecho=(total<1200)

#OUTPUT
print("###########################")
print("#BANCO DE LA NACION")
print("###########################")
print("#nombre del profesor :", nombre_del_profesor)
print("#sueldo              :", sueldo)
print("#descuento por afp   :", descuendo_por_afp)
print("#gastos mensuales    :", gastos_mesuales)
print("#total               :", total)
print("###########################")
print("¿profesor satisfecho?", profesor_satisfecho)
