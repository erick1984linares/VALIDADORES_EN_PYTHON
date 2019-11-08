#input
distancia=float(input("Ingrese el valor de la distancia:"))
vel1=float(input("Ingrese el valor de la velocidad del primer movil:"))
vel2=float(input("Ingrese el valor de la velocidad del segundo movil:"))

#processing
tiempo_encuentro=(distancia/(vel2+vel1))

#VERIFICADOR
tiempo_minimo=(tiempo_encuentro<10)

#output
print("                                                           ")
print("###########################################################")
print("#   CALCULADORA DEL TIEMPO DE ENCUENTRO DE DOS MOVILES    #")
print("###########################################################")
print("# El valor de la distancia es: ",distancia,"m")
print("# El valor de la velocidad del primer movil es:",vel1,"m/s")
print("# El valor de la velocidad del segunddo movil:",vel2,"m/s")
print("-----------------------------------------------------------")
print("# El valor del tiempo de encuentro de los moviles es:", tiempo_encuentro,"s")
print("###########################################################")
print("¿tiempo minimo?", tiempo_minimo)
