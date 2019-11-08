#input
densidad_liquido=float(input("Ingrese el valor del a densidad del liquido:"))
gravedad=float(input("Ingrese el valor de la gravedad:"))
profundidad=float(input("ingrese el valor de la profundidad a la que esta sumergido el cuerpo:"))

#processing
presion_hidrostatica=densidad_liquido*gravedad*profundidad

#VERIFICADOR
presion_alta=(presion_hidrostatica>=50)

#output
print("                                                              ")
print("##############################################################")
print("# CALCULADORA DE PRESION HIDROSTATICA DE UN CUERPO SUMERGIDO #")
print("##############################################################")
print("# El valor de la densidad del liquido es:",densidad_liquido)
print("# El valor de la gravedad es:",gravedad)
print("# El valor de la profundidad es:",profundidad)
print("#-------------------------------------------------------------")
print("# La presion hidrostatica a la que esta sometida el")
print("# cuerpo es de:",presion_hidrostatica)
print("##############################################################")
print("                                                              ")
print("¿presion alta?", presion_alta)
