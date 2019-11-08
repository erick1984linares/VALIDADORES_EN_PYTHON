#input
velocidad_inicial=float(input("Ingrese el valor de la velocidad inicial (m/s):"))
aceleracion=float(input("Ingrese el valor de la aceleracion(m/sº2):"))
tiempo=float(input("Ingrese el valor del tiempo (s):"))

#processing
distancia=(velocidad_inicial*tiempo)+(aceleracion*(tiempo**2))/2

#VERIFICADOR
distancia_absurda=(distancia<=400)

#output
print("                                                                ")
print("################################################################")
print("# CALCULADORA DE DISTANCIA DE UN MOVIL EN ACELERACION CONSTANTE ")
print("################################################################")
print("# El valor de la velocidad inicial es:",velocidad_inicial,"m/s")
print("# El valor de la aceleracion es:",aceleracion,"m/sº2")
print("# El valor del tiempo es de:",tiempo,"s")
print("#-----------------------------------------------------------")
print("# la distancia recorrida por el movil es de:",distancia,"m")
print("################################################################")
print("                                                                ")
print("¿distancia absurda?", distancia_absurda)
